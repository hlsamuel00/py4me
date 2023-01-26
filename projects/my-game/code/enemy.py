import pygame
from settings import *
from support import *
from entity import Entity

class Enemy(Entity):
    def __init__(self, monster_name, position, groups, obstacle_sprites, damage_player):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # Graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        # Movement setup
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # Stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        # Player interactions
        self.can_attack = True
        self.attack_cooldown = 400
        self.attack_time = None
        self.damage_player = damage_player

        # Invincibility timer
        self.vulnerable = True
        self.hit_time = None
        self.invicibility_duration = 300
        

    def import_graphics(self, name):
        enemy_path = f'./graphics/monsters/{name}/'
        self.animations = {
            'idle': [],
            'move': [],
            'attack': []
        }

        for animation in self.animations.keys():
            self.animations[animation] = import_folder(f'{enemy_path}{animation}')
        
    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index %= len(animation)

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        # Hit flicker
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_player_distance_and_direction(self, player):
        enemy_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)

        distance = (player_vector - enemy_vector).magnitude()
        
        if distance > 0:
            direction = (player_vector - enemy_vector).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        distance, _ = self.get_player_distance_and_direction(player)

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
            self.attack_time = pygame.time.get_ticks()
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self, player):
        if self.status == 'attack':
            self.damage_player(self.attack_damage, self.attack_type)
            self.attack_time = pygame.time.get_ticks()
        elif self.status == 'move':
            self.direction = self.get_player_distance_and_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def cooldowns(self):
        # Attack Cooldown
        current_time = pygame.time.get_ticks()
        if not self.can_attack:

            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        # Hit cooldown
        if not self.vulnerable:

            if current_time - self.hit_time >= self.invicibility_duration:
                self.vulnerable = True

    def enemy_update(self, player): 
        self.get_status(player)
        self.actions(player)
        self.check_death(player)

    def get_damage(self, player, attack_type):
        if self.vulnerable:
            self.direction = self.get_player_distance_and_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
            else:
                self.health -= player.get_full_magic_damage()
            
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance

    def check_death(self, player):
        if self.health <= 0:
            self.kill()
            player.exp += self.exp
            player.levelup()

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldowns()
    
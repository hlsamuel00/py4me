import pygame
from settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, destroy_attack, create_magic):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-30)

        # Graphics setup
        self.import_player_assets()
        self.status  = 'down'

        # Player movement
        self.attacking = False
        self.attack_cooldown = 200
        self.attack_time = None

        # Obstacles
        self.obstacle_sprites = obstacle_sprites

        # Weapons
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        # Magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        # Player Stats
        self.stats = { 'health': 100, 'energy': 60, 'attack': 10, 'magic': 4, 'speed': 5, 'level': 1 }
        self.max_stats = { 'health': 300, 'energy': 140, 'attack': 30, 'magic': 20, 'speed': 10 }
        self.upgrade_cost = {'health': 100, 'energy': 100, 'attack': 100, 'magic': 100, 'speed': 100}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 500
        self.speed = self.stats['speed']
        self.level = self.stats['level']

        # Damage interaction
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500

    def import_player_assets(self):
        character_path = './graphics/player/'
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle':[],
            'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack':[]
        }

        for animation in self.animations.keys():
            self.animations[animation] = import_folder(f'{character_path}{animation}')

    def input(self):
        #getting keys pressed from user
        keys = pygame.key.get_pressed()

        if not self.attacking:
            # Up and down movements
            if keys[pygame.K_UP]: 
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]: 
                self.direction.y = 1
                self.status = 'down'
            else: self.direction.y = 0

            # Left and right movements
            if keys[pygame.K_RIGHT]: 
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_LEFT]: 
                self.direction.x = -1
                self.status = 'left'
            else: self.direction.x = 0

            # Attack movements
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()

            # Magic movements
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                strength = magic_data[self.magic]['strength'] + self.stats['magic']
                cost = magic_data[self.magic]['cost']
                self.create_magic(self.magic, strength, cost)

            # Weapon switching
            if keys[pygame.K_q] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()
                self.weapon_index = (self.weapon_index + 1) % len(list(weapon_data.keys()))
                self.weapon = list(weapon_data.keys())[self.weapon_index]

            # Magic switching
            if keys[pygame.K_e] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()
                self.magic_index = (self.magic_index + 1) % len(list(magic_data.keys()))
                self.magic = list(magic_data.keys())[self.magic_index]            

    def get_status(self):
        # Idle status
        if not self.direction.x and not self.direction.y:
            if not 'idle' in self.status:
                if 'attack' in self.status: 
                    self.status = self.status.replace('attack', 'idle') 
                else:
                    self.status += '_idle'
        
        # Attacking status
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('idle', 'attack') 
                else:
                    self.status += '_attack'

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        # Attacking cooldown
        if self.attacking: 
            if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown']:
                self.attacking = False
                self.destroy_attack()

        # Weapon switch cooldown
        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        # Magic switch cooldown
        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True

        # Hit Cooldown
        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def animate(self): 
        animation = self.animations[self.status]

        # loop with the frame index
        self.frame_index += self.animation_speed
        self.frame_index %= len(animation)

        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        # flicker
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def levelup(self):
        exp_needed = nextLevel(self.level) 

        if self.exp >= exp_needed:
            self.exp %= exp_needed
            self.level += 1

    def get_full_weapon_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = weapon_data[self.weapon]['damage']

        return base_damage + weapon_damage

    def get_full_magic_damage(self):
        base_magic = self.stats['magic']
        spell_damage = magic_data[self.magic]['strength']

        return base_magic + spell_damage

    def energy_recovery(self): 
        if self.energy < self.stats['energy']:
            self.energy += 1 # .002 * self.stats['magic']
        else:
            self.energy = self.stats['energy']

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
        self.energy_recovery()

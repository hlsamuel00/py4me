import pygame
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-30)

        # Graphics setup
        self.import_player_assets()
        self.status  = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # Player movement
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 100
        self.attack_time = None

        # Obstacles
        self.obstacle_sprites = obstacle_sprites

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
                print('attack')

            # Magic movements
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                print('magic')

    def get_status(self):
        # Idle status
        if not self.direction.x and not self.direction.y:
            if not 'idle' in self.status:
                if 'attack' in self.status: 
                    self.status = self.status.replace('attack', 'idle') 
                else:
                    self.status += '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('idle', 'attack') 
                else:
                    self.status += '_attack'

    def move(self, speed):
        # Adjusting speed for diagonal movement
        if self.direction.magnitude() != 0: self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        # Correcting for collision on x-axis
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: self.hitbox.left = sprite.hitbox.right
        
        # Correcting for collision on y-axis
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking: 
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def animate(self): 
        animation = self.animations[self.status]

        # loop with the frame index
        self.frame_index += self.animation_speed
        self.frame_index %= len(animation)

        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)

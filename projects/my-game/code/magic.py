import pygame
from settings import *
from random import randint

class MagicPlayer():
    def __init__(self, animation_player):
        self.animation_player = animation_player


    def heal(self, player, strength, cost, groups):
        if player.energy >= cost and player.health < player.stats['health']:
            player.health += strength
            player.energy -= cost
            
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            
            self.animation_player.create_spell_particles('heal', player.rect.center + pygame.math.Vector2(0,-60), groups)
            self.animation_player.create_spell_particles('aura', player.rect.center, groups)

    def flame(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            
            player_direction = player.status.split('_')[0]

            if player_direction == 'right': direction = pygame.math.Vector2(1,0)
            elif player_direction == 'left': direction = pygame.math.Vector2(-1, 0)
            elif player_direction == 'up': direction = pygame.math.Vector2(0, -1)
            else: direction = pygame.math.Vector2(0, 1)

            for i in range(1, 6):
                flame_tile_size = TILESIZE * .75
                if direction.x:
                    offset_x = (direction.x * i) * flame_tile_size
                    x = player.rect.centerx + offset_x + randint(-flame_tile_size // 5 , flame_tile_size // 5)
                    y = player.rect.centery + randint(-flame_tile_size // 5 , flame_tile_size // 5)
                else:
                    offset_y = (direction.y * i) * flame_tile_size 
                    x = player.rect.centerx + randint(-flame_tile_size // 5 , flame_tile_size // 5)
                    y = player.rect.centery + offset_y + randint(-flame_tile_size // 5 , flame_tile_size // 5)
                    
                self.animation_player.create_spell_particles('flame', (x,y), groups)
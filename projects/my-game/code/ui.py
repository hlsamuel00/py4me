import pygame
from settings import *

class UI:
    def __init__(self):
        # General info
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # Bar setup
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 42, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # Weapon display setup
        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon['graphic']
            weapon_image = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon_image)

        # Magic display setup
        self.magic_graphics = []
        for magic in magic_data.values():
            path = magic['graphic']
            magic_image = pygame.image.load(path).convert_alpha()
            self.magic_graphics.append(magic_image)

    def show_bar(self, current_amount, max_amount, bg_rect, color, text):
        # draw background
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect, border_radius = 4)

        # converting stat to pixels
        ratio = current_amount / max_amount
        current_width = bg_rect.width * ratio
        current_rect = pygame.Rect(bg_rect.left, bg_rect.top, current_width, bg_rect.height)

        # get bar text
        font_surface = pygame.font.Font(UI_FONT, 11).render(text, True, TEXT_COLOR)
        font_rect = pygame.Rect(bg_rect.left + 7, bg_rect.top + 11, font_surface.get_width(), BAR_HEIGHT)
        
        # draw the bars
        pygame.draw.rect(self.display_surface, color, current_rect, border_radius = 4)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 4, border_radius = 4)

        # draw the labels 
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, font_rect.inflate(7.5, 0), border_radius = 4)
        self.display_surface.blit(font_surface, font_surface.get_rect(center = font_rect.center))

    def show_exp(self, exp):
        text_surface = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surface.get_rect(bottomright = (x,y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(10, 10), border_radius = 4)
        self.display_surface.blit(text_surface, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(10, 10), 4, border_radius = 4)

    def selection_box(self, left, top, text, has_switched):
        # draw boxes
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect, border_radius = 8)
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 4, border_radius = 8)
        else: 
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 4, border_radius = 8)

        # draw labels
        font_surface = pygame.font.Font(UI_FONT, 11).render(text, True, TEXT_COLOR)
        font_rect = font_surface.get_rect(centerx = bg_rect.centerx, y = bg_rect.y - 20)

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, font_rect.inflate(17.5, 10), border_radius = 4)
        self.display_surface.blit(font_surface, font_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, font_rect.inflate(17.5, 10), 4, border_radius = 4)

        return bg_rect

    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, self.display_surface.get_size()[1] - 100, 'weapon', has_switched)
        weapon_surface = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(weapon_surface, weapon_rect)

    def magic_overlay(self, magic_index, has_switched):
        bg_rect = self.selection_box(100, self.display_surface.get_size()[1] - 100 , 'magic', has_switched)
        magic_surface = self.magic_graphics[magic_index]
        magic_rect = magic_surface.get_rect(center = bg_rect.center)

        self.display_surface.blit(magic_surface, magic_rect)


    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR, 'Health')
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR, 'Energy')
        # self.show_bar(player.exp, player.stats['exp_next'], self.exp_bar_rect, EXP_COLOR, 'Exp')

        self.show_exp(player.exp)

        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        self.magic_overlay(player.magic_index, not player.can_switch_magic)
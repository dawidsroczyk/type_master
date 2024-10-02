import pygame


class Button:

    def __init__(self, x, y, width, height, text, font, color, text_color,
                 scene_manager):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.color = color
        self.text_color = text_color

        self.scene_manager = scene_manager

        self.rect = pygame.Rect(x, y, width, height)
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)


    def draw(self, screen):

        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def check_press(self, events: list):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.press_action()


    def press_action(self):
        raise NotImplemented()
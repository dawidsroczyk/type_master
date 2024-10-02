from .test_song_scene import TestSongScene
from ..class_bases.base_scene import *

class TitleScene(BaseScene):


    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.font = pygame.font.Font(None, 74)  # Font for the title
        self.button_font = pygame.font.Font(None, 48)  # Font for the button
        self.button_rect = pygame.Rect(250, 300, 300, 100)


    def update(self):
        pass


    def render(self, screen):
        screen.fill((255, 0, 0))

        title_surface = self.font.render("Title scene", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(400, 200))
        screen.blit(title_surface, title_rect)

        # Render button
        pygame.draw.rect(screen, (0, 255, 0), self.button_rect)  # Draw button
        button_text = self.button_font.render("Play test song", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        screen.blit(button_text, button_text_rect)


    def process_input(self, events, pressed_keys):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.button_rect.collidepoint(event.pos):
                new_scene = TestSongScene(self.scene_manager)
                self.scene_manager.change_scene(new_scene)

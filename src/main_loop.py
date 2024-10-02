import pygame
import src.constants as const
from src.classes.scene_manager import SceneManager


def main_loop(scene_manager):
    # pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while scene_manager.active_scene is not None:

        active_scene = scene_manager.active_scene

        pressed_keys = pygame.key.get_pressed()

        filtered_events = []
        for event in pygame.event.get():
            filtered_events.append(event)

        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.render(screen)

        pygame.display.flip()
        clock.tick(const.FPS)

    pass
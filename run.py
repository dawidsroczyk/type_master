from src.classes.scene_manager import SceneManager
from src.main_loop import main_loop
from src.scenes.title_scene import TitleScene
import pygame

def run_app():
    pygame.init()
    scene_manager = SceneManager()
    main_loop(scene_manager)

if __name__ == '__main__':
    run_app()

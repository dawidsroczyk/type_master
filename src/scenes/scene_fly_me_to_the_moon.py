import pygame

from src.scenes.song_scene import SongScene


class SceneFlyMeToTheMoon(SongScene):
    
    def __init__(self, scene_manager):
        super().__init__('fly_me_to_the_moon', scene_manager)


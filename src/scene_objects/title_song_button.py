import pygame

from src.constants import SONG_BUTTON_WIDTH, SONG_BUTTON_HEIGHT
from src.scene_objects.button import Button
from src.scenes.test_song_scene import TestSongScene


class SongButton(Button):

    def __init__(self,x: int, y: int, song_name: str, scene_manager):
        self.font = pygame.font.Font(None, 48)
        super().__init__(x, y, SONG_BUTTON_WIDTH, SONG_BUTTON_HEIGHT, song_name,
                         self.font, (0,255,0), (0,0,0), scene_manager)

    def press_action(self):
        new_scene = TestSongScene(self.scene_manager)
        self.scene_manager.change_scene(new_scene)
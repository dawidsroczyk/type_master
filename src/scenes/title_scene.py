from .scene_fly_me_to_the_moon import SceneFlyMeToTheMoon
from .test_song_scene import TestSongScene
from ..class_bases.base_scene import *
from ..constants import SONG_BUTTON_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT
from ..scene_objects.title_song_button import SongButton
import os


class TitleScene(BaseScene):


    def __init__(self, scene_manager):
        super().__init__(scene_manager)

        titles = [
            ('Fly me to the moon', SceneFlyMeToTheMoon),
            ('My darling Clementine', TestSongScene),
            ('All star', TestSongScene)
        ]

        self.song_buttons = []
        x_start = 10
        y_start = 30
        for idx, title in enumerate(titles):
            new_button = SongButton(x_start,
                                    y_start + idx * (SONG_BUTTON_HEIGHT + 10),
                                    title[0],
                                    scene_manager,
                                    title[1])
            self.song_buttons.append(new_button)

        background_image = pygame.image.load(os.path.join('resources', 'coffee_shop.png'))
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image = background_image


    def update(self):
        pass


    def render(self, screen):
        #screen.fill((255, 0, 0))
        screen.blit(self.background_image, (0, 0))

        for song_button in self.song_buttons:
            song_button.draw(screen)


    def process_input(self, events, pressed_keys):

        for song_button in self.song_buttons:
            song_button.check_press(events)

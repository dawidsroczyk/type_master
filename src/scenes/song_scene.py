from ..class_bases.base_scene import *
from ..scene_objects.button import Button
from ..scene_objects.title_song_button import SongButton


class SongScene(BaseScene):

    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.buttons = []

        self.buttons.append(GoToTitleButton(scene_manager))


    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 255))

        for button in self.buttons:
            button.draw(screen)



    def process_input(self, events, pressed_keys):

        for button in self.buttons:
            button.check_press(events)

###

class GoToTitleButton(Button):

    def __init__(self, scene_manager):
        self.font = pygame.font.Font(None, 48)
        super().__init__(0, 0, 20, 20, '', self.font,
                         (255, 255, 0), (0, 0, 0), scene_manager)

    def press_action(self):
        self.scene_manager.go_to_title()

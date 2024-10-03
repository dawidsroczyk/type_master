from ..class_bases.base_scene import *
from ..constants import SONG_TEXT_HEIGHT
from ..scene_objects.button import Button
from ..scene_objects.song_text import SongText
from ..scene_objects.title_song_button import SongButton
import os
from itertools import chain


class SongScene(BaseScene):

    def __init__(self, song_name, scene_manager):
        super().__init__(scene_manager)
        self.song_name = song_name

        self.buttons = []
        self.buttons.append(GoToTitleButton(scene_manager))

        self.text_y = 100
        self.song_texts = []
        self.texts = []

        '''
        self.texts.append(SongText(100, 'Fly me to the moon'))
        self.texts[-1].choose_letter(0)
        self.texts.append(SongText(100 + SONG_TEXT_HEIGHT, 'Let me play among the stars'))
        self.texts[-1].choose_letter(-1)
        '''

        with open(os.path.join('songs', song_name+'.txt')) as file:
            self.lyrics = file.readlines()
            self.lyrics = [x.rstrip().replace('.', '').replace(',', '').split() for x in self.lyrics]

        with open(os.path.join('songs', song_name + '_output.txt'), 'r') as file:
            lines = file.readlines()
            lines = [x.rstrip().split(' ') for x in lines]

            count = 0
            for row, line in enumerate(self.lyrics):
                for col, word in enumerate(line):
                    start = float(lines[count][0])
                    end = float(lines[count][1])
                    self.lyrics[row][col] = {'start': start, 'end': end, 'word': self.lyrics[row][col]}
                    count += 1

        for lyrics_line in self.lyrics:
            self.add_text_line(lyrics_line)

        self.current_line_idx = 0
        self.song_texts[0].choose_letter(0)
        self.song_texts[0].set_active()

    def add_text_line(self, lyrics_line):
        str_line = ' '.join([x['word'] for x in lyrics_line])
        new_song_text = SongText(self.text_y, str_line, self)
        self.texts.append(new_song_text)
        self.song_texts.append(new_song_text)
        self.text_y += SONG_TEXT_HEIGHT

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 255))

        for text in self.texts:
            text.draw(screen)

        for button in self.buttons:
            button.draw(screen)

    def move_to_next_line(self):

        self.song_texts[self.current_line_idx].set_not_active()

        self.current_line_idx += 1

        self.song_texts[self.current_line_idx].choose_letter(0)
        self.song_texts[self.current_line_idx].set_active()

    def process_input(self, events, pressed_keys):

        for button in self.buttons:
            button.check_press(events)

        for text in self.texts:
            text.process_input(events, pressed_keys)

###

class GoToTitleButton(Button):

    def __init__(self, scene_manager):
        self.font = pygame.font.Font(None, 48)
        super().__init__(0, 0, 20, 20, '', self.font,
                         (255, 255, 0), (0, 0, 0), scene_manager)

    def press_action(self):
        self.scene_manager.go_to_title()

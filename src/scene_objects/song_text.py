# from pygame.examples.video import event

from src.constants import SONG_TEXT_OFFSET, SCREEN_WIDTH, SONG_TEXT_HEIGHT
from src.scene_objects.text import Text
import pygame
import random

class SongText(Text):

    def __init__(self ,y: int, text: str, song_scene):
        # super().__init__(SONG_TEXT_OFFSET, y, SCREEN_WIDTH - 2 * SONG_TEXT_OFFSET, SONG_TEXT_HEIGHT, text)
        self.font = pygame.font.Font(None, 74)
        self.song_scene = song_scene
        self.active = False
        self.highlighted_idx = -1

        self.chars = []
        self.words = []
        full_text_length = calculate_text_length(text, self.font)
        cur_x = SONG_TEXT_OFFSET + (SCREEN_WIDTH - 2 * SONG_TEXT_OFFSET - full_text_length) // 2
        cur_word = []
        for char in text:
            char_width = calculate_text_length(char, self.font)
            char_text = Text(cur_x, y, char_width, SONG_TEXT_HEIGHT, char)
            if char != ' ':
                self.words.append(cur_word)
                cur_word = []
                self.chars.append(char_text)
            cur_x += char_width
            cur_word.append(char)
        if len(cur_word) > 0:
            self.words.append(cur_word)

    def draw(self, screen):

        for char in self.chars:
            char.draw(screen)

    # idx - idx of yellow char
    # -1 to all black
    # len(self.chars) to all white
    def choose_letter(self, idx: int):

        if idx > len(self.chars):
            idx = len(self.chars)
        if idx < -1:
            idx = -1

        self.highlighted_idx = idx

        if idx == -1:
            for char in self.chars:
                char.set_color((0, 0, 0))
            return
        if idx == len(self.chars):
            for char in self.chars:
                char.set_color((255, 255, 255))

        for char in self.chars[:idx]:
            char.set_color((255, 255, 255))

        if idx == len(self.chars):
            return

        self.chars[idx].set_color((255, 255, 0))

        for char in self.chars[idx+1:]:
            char.set_color((0, 0, 0))


    def process_input(self, events, pressed_keys):

        if self.active:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key).lower()
                    if key == self.chars[self.highlighted_idx].text.lower():
                        self.move_next_char()

    def move_next_char(self):
        self.highlighted_idx += 1
        self.choose_letter(self.highlighted_idx)

        if self.highlighted_idx == len(self.chars):
            self.song_scene.move_to_next_line()

    def set_active(self):
        self.active = True

    def set_not_active(self):
        self.active = False


def calculate_text_length(text: str, font: pygame.font):
    temp_text = font.render(text, True, (0, 0, 0))
    temp_text_width, temp_text_height = temp_text.get_size()
    return temp_text_width
import pygame

class Text:

    def __init__(self, x: int ,y: int, width: int, height: int, text: str):
        self.font = pygame.font.Font(None, 74)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_render = None
        self.text_color = (0, 0, 0)

    def draw(self, screen):

        text = self.font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=(self.x + self.width//2, self.y + self.height//2))
        screen.blit(text, text_rect)

    def set_pos(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_text(self, text: str):
        self.text = text

    def process_input(self, events, pressed_keys):
        pass

    def set_color(self, color=(0,0,0)):
        self.text_color = color

    def text_width(self):

        if self.text_render is None:
            return -1

        width, height = self.text_render.get_size()
        return width
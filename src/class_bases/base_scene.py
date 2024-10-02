import pygame

class BaseScene:

    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
    
    def process_input(self, events, pressed_keys):
        raise NotImplemented()
    
    def update(self):
        raise NotImplemented()
    
    def render(self, screen):
        raise NotImplemented

    def terminate(self):
        self.scene_manager.change_scene(None)


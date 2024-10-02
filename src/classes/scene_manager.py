from ..class_bases.base_scene import *
from ..scenes.title_scene import TitleScene


class SceneManager:

    def __init__(self):
        self.active_scene: BaseScene = self.create_title_scene()

    def create_title_scene(self) -> TitleScene:
        return TitleScene(scene_manager=self)

    def change_scene(self, new_scene: BaseScene):
        self.active_scene = new_scene
    
    def go_to_title(self):
        new_scene = self.create_title_scene()
        self.change_scene(new_scene)

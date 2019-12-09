from engine.vision.Scene import Scene
from engine.vision.Renderer import Renderer
import time


class Game:

    renderer = None
    behaviours = []
    on = True

    @staticmethod
    def prepare():
        scene = Scene(10, 50)
        Game.renderer = Renderer()
        Game.renderer.load_scene(scene)
        for behaviour in Game.behaviours:
            behaviour.start()

    @staticmethod
    def play():
        while Game.on:
            for behaviour in Game.behaviours:
                behaviour.before_scene_calculate()

            Game.renderer.scene.clear()
            Game.renderer.calculate_objects()
            Game.renderer.render()

            time.sleep(0.1)

    @staticmethod
    def end():
        if Game.on:
            Game.on = False

        for behaviour in Game.behaviours:
            behaviour.end()

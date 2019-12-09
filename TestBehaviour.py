from engine.game.Behaviour import Behaviour
from engine.game.Game import Game
from engine.vision.Object import Object
from engine.vision.sprite.Sprite import Sprite
from engine.vision.sprite.SpriteLoader import SpriteLoader


class TestBehaviour(Behaviour):

    def __init__(self):
        super().__init__()
        self.obj = Object()

    def start(self):
        sprite = SpriteLoader.load('asset/saloon.spr')
        sprite.debug_render()
        self.obj.sprite = sprite
        Game.renderer.add_object(self.obj)

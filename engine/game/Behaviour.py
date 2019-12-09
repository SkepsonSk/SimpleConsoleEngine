from engine.game.Game import Game


class Behaviour:

    def __init__(self):
        Game.behaviours.append(self)

    # -------------------- Game state change events --------------------

    def start(self):
        pass

    def end(self):
        pass

    # -------------------- Game update events --------------------

    def before_scene_calculate(self):
        pass

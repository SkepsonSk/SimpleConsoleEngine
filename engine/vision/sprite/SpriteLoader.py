from engine.vision.sprite.Sprite import Sprite


class SpriteLoader:

    @staticmethod
    def load(sprite_path):
        sprite_file = open(sprite_path, 'r')
        dim = sprite_file.readline().split(';')

        width = int(dim[0])     # 10
        height = int(dim[1])    # 4

        sprite = Sprite(width, height)
        for x in range(width):
            row = sprite_file.readline()
            for y in range(height):
                sprite.set_point(x, y, ' ' + '&' + ' ')
        return sprite






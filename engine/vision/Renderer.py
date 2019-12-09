from os import system


class Renderer:

    active = None

    def __init__(self):
        if Renderer.active is not None:
            raise RuntimeError('Renderer has already been initialized.')
        else:
            self.scene = None
            self.objects = []
            self.menu = None
            Renderer.active = self

    # -----------------------------------------------------

    def load_scene(self, scene):
        self.scene = scene

    def add_object(self, ob):
        self.objects.append(ob)

    # -----------------------------------------------------

    def calculate_objects(self):
        for obj in self.objects:
            start_x = obj.x
            start_y = obj.y
            sprite = obj.sprite
            for x in range(sprite.width):

                if x + start_x >= self.scene.height:
                    break

                for y in range(sprite.height):
                    if y + start_y >= self.scene.width:
                        break
                    self.scene.matrix[start_y + y][start_x + x] = sprite.matrix[y][x]

    def render(self):
        if self.scene is None:
            raise RuntimeError('No scene has been loaded to the Renderer')
        else:
            system('cls')
            for y in range(len(self.scene.matrix)):
                for x in range(len(self.scene.matrix[y])):
                    print(self.scene.matrix[y][x], end='')
                print()

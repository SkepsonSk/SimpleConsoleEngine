class Scene:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [' '] * width
        i = 0
        while i < len(self.matrix):
            self.matrix[i] = ['  '] * height
            i += 1

    def clear(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                self.matrix[y][x] = ' # '

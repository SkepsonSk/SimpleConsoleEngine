class Sprite:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [''] * width
        i = 0
        while i < len(self.matrix):
            self.matrix[i] = ['&'] * height
            i += 1

    def set_point(self, x, y, c):
        print(str(x) + ':' + str(y) + " / " + str(len(self.matrix)) + ":" + str(len(self.matrix[0])))
        self.matrix[x][y] = str(c)

    def debug_render(self):
        i = 0
        while i < len(self.matrix):
            j = 0
            while j < len(self.matrix[i]):
                print(self.matrix[i][j], end='')
                j += 1
            i += 1
            print()

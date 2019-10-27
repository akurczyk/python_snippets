from abc import ABCMeta, abstractmethod
from PIL import Image, ImageDraw


class Drawable(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, canvas):
        pass


class Colorable:
    def __init__(self, color):
        self.color = color


class Point(Drawable, Colorable):
    def __init__(self, x, y, color=(0, 0, 0)):
        Colorable.__init__(self, color)
        self.x = x
        self.y = y

    def draw(self, canvas):
        canvas.point((self.x, self.y), self.color)


class Line(Drawable, Colorable):
    def __init__(self, p1, p2, color=(0, 0, 0)):
        super().__init__(color)
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas):
        canvas.line([(self.p1.x, self.p1.y), (self.p2.x, self.p2.y)], self.color)


class Rectangle(Drawable, Colorable):
    def __init__(self, p1, p2, color=(0, 0, 0)):
        super().__init__(color)
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas):
        p12 = Point(self.p1.x, self.p2.y)
        p21 = Point(self.p2.x, self.p1.y)

        Line(self.p1, p12, color=self.color).draw(canvas)
        Line(p12, self.p2, color=self.color).draw(canvas)
        Line(self.p2, p21, color=self.color).draw(canvas)
        Line(p21, self.p1, color=self.color).draw(canvas)


if __name__ == '__main__':
    point = Point(25, 25, color=(255, 0, 0))
    line = Line(Point(50, 50), Point(150, 150), color=(0, 255, 0))
    rectangle = Rectangle(Point(75, 75), Point(125, 125), color=(0, 0, 255))

    image = Image.new('RGB', (200, 200), (255, 255, 255))
    canvas = ImageDraw.Draw(image)

    point.draw(canvas)
    line.draw(canvas)
    rectangle.draw(canvas)

    image = image.resize((800, 800), Image.NEAREST)
    image.show()

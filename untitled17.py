from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


circle = Circle(radius=5)

circle_area = circle.calculate_area()
print(f"as Circle;;{circle_area}")
rectangle = Rectangle(width=10, height=20)
rectangle_area = rectangle.calculate_area()
print(f"as rectangle: {rectangle_area}")

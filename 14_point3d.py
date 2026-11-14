
import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print("3D Point:", (self.x, self.y, self.z))

    def distance(self, p):
        return math.sqrt(
            (self.x - p.x)**2 +
            (self.y - p.y)**2 +
            (self.z - p.z)**2
        )


p1 = Point3D(1, 2, 3)
p2 = Point3D(4, 5, 6)

p1.display()
p2.display()

print("Distance:", p1.distance(p2))


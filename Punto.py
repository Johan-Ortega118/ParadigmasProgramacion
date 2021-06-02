#Punto
#Johan Paul Ortega Murillo
#S19004894 ISW

class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x}, {self.y})"
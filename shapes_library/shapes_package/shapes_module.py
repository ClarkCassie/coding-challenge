import math


class Circle:
    """
    This class implements the Circle API
    """
    def __init__(self, radius: float = None):
        validateCircleRadius(radius)
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)


class Rectangle:
    """
    This class implements the Rectangle API
    """
    def __init__(self, height: float = None, width: float = None):
        
        if width is None or width <= 0:    
                raise ValueError("Supplied width and height must be > 0")
        self.width = width
       
        if height is None or height < 0:
                raise ValueError("Supplied width and height must be > 0")
        self.height = height

    
        
    def area(self):
        return round(self.height * self.width, 2)


class Capital:
    """
    This class implements the Capital API
    """
    def __init__(self, name: str = "abcd"):
        if name[0].islower:
            raise ValueError("Supplied name must start with capital letter")
        self.name = name    





def validateCircleRadius(radius):
    if radius is None or radius <= 0:
        raise ValueError("Supplied radius must be > 0")

        
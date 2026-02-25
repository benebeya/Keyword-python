#super() = function used in a child class to call methods from a parent class (superclass)
#  Allows you to extend the functionality of the inherited methods 

class Shap :
    def __init__(self, color , is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe (self):
        print(f"It is {self.color} and {'filled'if self.is_filled else 'not fielld'}")


class Circle(Shap) :
    def __init__(self, color , is_filled , radius ):
        super().__init__(color, is_filled)
        self.radius = radius 
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()
        
class Square (Shap):
    def __init__(self, color , is_filled , width ):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        
        
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()
        
    
class Triangle(Shap) :
    def __init__(self, color , is_filled, width , height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        
    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2 }cm^2")
        super().describe()
        
        
circle = Circle("red",True,5)
square = Square("blue", False,6)
triangle = Triangle("yellow",True, 7,8)

triangle.describe()

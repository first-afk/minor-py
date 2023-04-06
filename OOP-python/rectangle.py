class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self):
        # area = int(area)
        
        print(f'area = {self.height * self. width}')

    def perimeter(self):
        print(f'perimeter = {2 * (self.height + self.width)}')    
 
rec = Rectangle(24, 2)
rec.area() 
rec.perimeter()
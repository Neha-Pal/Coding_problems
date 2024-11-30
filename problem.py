class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y)

A = Point(3, 4)
B = Point(1, 2)

C = A + B

print(f"C.X = {C.x}") 
print(f"C.Y = {C.y}")  

class Point:
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
    
    def __str__(self):
        return f"X: {self.x_cord}, Y: {self.y_cord}"

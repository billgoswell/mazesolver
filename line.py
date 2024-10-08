
class Line:
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2

    def __str__(self):
        return f"X1: {self.p1.x_cord}, Y1: {self.p1.y_cord}, X2: {self.p2.x_cord}, Y2: {self.p2.y_cord}"

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x_cord, self.p1.y_cord, self.p2.x_cord, self.p2.y_cord, fill=fill_color, width=2)


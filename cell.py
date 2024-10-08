from line import Line
from point import Point
from window import Window


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win
        self.visited = False
        

    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win is None:
            return
        left_line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.__win.draw(left_line, "black")
        else:
            self.__win.draw(left_line, "white")
            
        right_line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.__win.draw(right_line, "black")
        else:
            self.__win.draw(right_line, "white")

        top_line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.__win.draw(top_line, "black")       
        else:
            self.__win.draw(top_line, "white")
            
        bottom_line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.__win.draw(bottom_line, "black")
        else:
            self.__win.draw(bottom_line, "white")

    def draw_move(self, to_cell, undo=False):
        x_start = (self.__x1 + self.__x2)/2
        y_start = (self.__y1 + self.__y2)/2
        x_end = (to_cell.__x1 + to_cell.__x2)/2
        y_end = (to_cell.__y1 + to_cell.__y2)/2
        line = Line(Point(x_start, y_start), Point(x_end, y_end))
        if not undo:
            self.__win.draw(line, "red")
        else:
            self.__win.draw(line, "grey")


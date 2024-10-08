from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win_height = 800
    win_width = 600
    num_rows = 10
    num_cols = 10
    x_offset = 10
    y_offset = 10
    height_cols = (win_height - (y_offset*2))/num_cols
    width_rows = (win_width - (x_offset*2))/num_rows
    
    win = Window(win_height, win_width)
    maze = Maze(x_offset, y_offset, num_rows, num_cols, height_cols, width_rows, win)
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()

main()


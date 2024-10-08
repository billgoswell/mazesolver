from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self.seed = None 

        
    def _create_cells(self):
        for i in range(0, self._num_cols):
            self._cells.append([])
            for j in range(0, self._num_rows):
                cell = Cell(self._win)
                self._cells[i].append(cell)
                self._draw_cell(i, j)
        self._animate()

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1_loc = self._x1 + j*self._cell_size_x
        x2_loc = x1_loc + self._cell_size_x
        y1_loc = self._y1 + i*self._cell_size_y
        y2_loc = y1_loc + self._cell_size_y
        self._cells[i][j].draw(x1_loc, x2_loc, y1_loc, y2_loc)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(.5)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols -1][self._num_rows -1].has_bottom_wall = False
        self._draw_cell(self._num_cols -1, self._num_rows -1) 

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_Visit = []
            if(i+1 < self._num_cols):
                if not (self._cells[i+1][j].visited):
                    to_Visit.append([i+1, j])
            if(i-1 >= 0):
                if not (self._cells[i-1][j].visited):
                    to_Visit.append([i-1, j])
            if(j+1 < self._num_rows):
                if not (self._cells[i][j+1].visited):
                    to_Visit.append([i, j+1])
            if(j-1 >= 0):
                if not (self._cells[i][j-1].visited):
                    to_Visit.append([i, j-1])
            if len(to_Visit) == 0:
                self._draw_cell(i, j)
                return
            next = None
            if self.seed == None:
                next = to_Visit[random.randrange(0, len(to_Visit))]
            else:
                next = to_Visit[self.seed]

            if next[0] == i:
                if next[1] == j+1:
                    self._cells[i][j].has_right_wall = False
                    self._break_walls_r(i, j+1)
                if next[1] == j-1:
                    self._cells[i][j].has_left_wall = False
                    self._break_walls_r(i, j-1)
            if next[0] == i+1:
                self._cells[i][j].has_bottom_wall = False
                self._break_walls_r(i+1, j)
            if next[0] == i-1:
                self._cells[i][j].has_top_wall = False
                self._break_walls_r(i-1, j)

    def _reset_cells_visited(self): 
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._cells[i][j].visited = False
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        if (i == self._num_cols - 1) and (j == self._num_rows -1):
            return True
        self._cells[i][j].visited = True
        self._animate()
        if (i-1 >= 0) and (not self._cells[i-1][j].visited) and (not self._cells[i][j].has_top_wall):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        if (i+1 < self._num_cols) and (not self._cells[i+1][j].visited) and (not self._cells[i][j].has_bottom_wall):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        if (j-1 >= 0) and (not self._cells[i][j-1].visited) and (not self._cells[i][j].has_left_wall):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        if (j+1 < self._num_rows) and (not self._cells[i][j+1].visited) and (not self._cells[i][j].has_right_wall):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        return False
       

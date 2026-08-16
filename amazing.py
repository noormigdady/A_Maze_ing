import random

class Cell:
    def __init__(self, i, j):
        self.top = True
        self.bottom = True
        self.right = True
        self.left = True
        self.visited = False
        self.i = i
        self.j = j

def create_grid(height, width):
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append("#")
        grid.append(row)
    return grid

def Next_cell(grid, cell, direction):
    if direction == "top":
        i = cell.i - 1
    if direction == "bottom":
        i = cell.i + 1
    if direction == "right":
        j = cell.j + 1
    if direction == "left":
        j = cell.j - 1

    return grid[i][j]

def valid(grid, cell, direction):
    #locked = lock_42(grid, height, width)
    next_cell = Next_cell(grid, cell,direction)
    if next_cell.visited:# or next_cell in locked:
        return False
    return True

def where_to(grid, cell):
    directions = ["top", "bottom", "right", "left"]
    if cell.i == 0:
        directions.remove("top")
    if cell.i == height - 1:
        directions.remove("bottom")
    if cell.j == 0:
        directions.remove("left")
    if cell.j == width - 1:
        dirctions.remove("right")
    while True:
        direction = random.choice(directions)
        if valid(grid, cell, direction):
            return direction
        else:
            directions.remove(direction)
            if len(directions) == 0:
                return None

def move(grid, cell, direction):
    next_cell = Next_cell(grid, cell, direction)
    if direction == "top":
        cell.top = False
        next_cell.bottom = False
    if direction == "bottom":
        cell.bottom = False
        next_cell.top = False
    if direction == "right":
        cell.right = False
        next_cell.left = False
    if direction == "left":
        cell.left = False
        next_cell.right = False
    next_cell.visited = True
    return next_cell

def generate_maze(grid, height, width):
    i = 0
    j = 0
    track = []
    cell = maze[i][j]
    cell.visited = True
    visited_cells = 1
    while visited_cells != height * width:
        direction = where_to(grid)
        if direction == None:
            track.pop()
            if len(track) == 0:
                break
            cell = track[-1]
        else:
            next_cell = move(grid, cell, direction)
            visited_cells += 1
            cell = next_cell
            track.append(cell)
    return grid

def main():
    width = 10
    height = 10
    grid = create_grid(height, width)
main()

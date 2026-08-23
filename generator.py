import random


class Cell():
    def __init__(self, i, j):
        self.top = True
        self.bottom = True
        self.right = True
        self.left = True
        self.visited = False
        self.locked = False
        self.i = i
        self.j = j


class MazeGenerator():
    def __init__(self, height, width):
        self.grid = []
        self.height = height 
        self.width = width
        for i in range(width):
            row = []
            for j in range(height):
                row.append(Cell(i, j))
            self.grid.append(row)

    def Next_cell(self, cell, direction):
        i = cell.i
        j = cell.j
        if direction == "top":
            i = cell.i - 1
        if direction == "bottom":
            i = cell.i + 1
        if direction == "right":
            j = cell.j + 1
        if direction == "left":
            j = cell.j - 1
        return self.grid[i][j]

    def valid(self, cell, direction):
        next_cell = self.Next_cell(cell, direction)
        if next_cell.visited or next_cell.locked:
            return False
        return True

    def where_to(self, cell):
        directions = ["top", "bottom", "right", "left"]
        if cell.i == 0:
            directions.remove("top")
        if cell.i == self.height - 1:
            directions.remove("bottom")
        if cell.j == 0:
            directions.remove("left")
        if cell.j == self.width - 1:
            directions.remove("right")

        while True:
            direction = random.choice(directions)
            if self.valid(cell, direction):
                return direction
            else:
                directions.remove(direction)
                if len(directions) == 0:
                    return None

    def move(self, cell, direction):
        next_cell = self.Next_cell(cell, direction)
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

    def generator(self, entry):
        i, j = entry
        track = []
        track.append(self.grid[i][j])
        cell = self.grid[i][j]
        cell.visited = True
        visited_cells = 1
        if self.width < 11 or self.height < 9:
            size = self.height * self.width
        else:
            size = self.height * self.width - 18

        while visited_cells != size:
            direction = self.where_to(cell)
            if direction is None:
                track.pop()
                if len(track) == 0:
                    break
                cell = track[-1]
            else:
                next_cell = self.move(cell, direction)
                visited_cells += 1
                cell = next_cell
                track.append(cell)
        return self.grid

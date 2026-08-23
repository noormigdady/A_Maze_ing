DIR = {
        "top": "N",
        "bottom": "S",
        "right": "E",
        "left": "W"
        }

def Next_cell(grid, cell, direction):
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
    return grid[i][j]


def where_to(grid, cell, height, width):
    directions = ["top", "bottom", "right", "left"]
    if cell.i == 0:
        directions.remove("top")
    if cell.i == height - 1:
        directions.remove("bottom")
    if cell.j == 0:
        directions.remove("left")
    if cell.j == width - 1:
        directions.remove("right")

def valid(maze, cell, direction):
    if direction == "top":
        if not cell.top:
            return True
        return False
    if direction == "bottom":
        if not cell.bottom:
            return True
        return False
    if direction == "left":
        if not cell.left:
            return True
        return False
    if direction == "right":
        if not cell.right:
            return True
        return False


def find_path(maze, height, width, entry, Exit, sequence):
    i, j = entry
    x, y = Exit
    path = []
    cell = maze[i][j]
    path.append(cell)

    while i != x and j != y:
        direction = where_to(maze, cell, height, width)
        if direction is None:
            path.pop()
            if len(path) == 0:
                break
            cell = path[-1]
        else:
            if valid(maze, cell, direction):
                next_cell = Next_cell(maze, cell, direction)
                sequence += DIR[direction]
                cell = next_cell
                path.append(cell)
                if (cell.i, cell.j) == Exit:
                    break
    return path




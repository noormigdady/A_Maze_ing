class Cell:
    def __init__(self, x, y):
        self.dx = x
        self.dy = y
        self.directions = {
            "north": True,
            "south": True,
            "east": True,
            "west": True
        }
        self.visited = False

    def is_visited(self) -> bool:
        if self.visited:
            return True
        return False

    def visit_cell(current_cell, next_cell) -> None:
        if current_cell.dx > next_cell.dx and current_cell.dy == next_cell.dy:
            current_cell.directions["east"] = False
            next_cell.directions["west"] = False
            next_cell.visited = True
        elif current_cell.dx < next_cell.dx and current_cell.dy == next_cell.dy:
            current_cell.directions["west"] = False
            next_cell.directions["east"] = False
            next_cell.visited = True
        elif current_cell.dx == next_cell.dx and current_cell.dy > next_cell.dy:
            current_cell.directions["north"] = False
            next_cell.directions["south"] = False
            next_cell.visited = True
        elif current_cell.dx == next_cell.dx and current_cell.dy < next_cell.dy:
            current_cell.directions["south"] = False
            next_cell.directions["next"] = False
            next_cell.visited = True

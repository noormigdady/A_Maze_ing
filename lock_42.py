def lock_42(grid, height, width):
    if width < 11 or height < 9:
        return
    i = height // 2
    j = width // 2
    # grid[i - 1][j - 1].locked = True
    # grid[i - 2][j - 1].locked = True
    grid[i][j - 1].locked = True
    grid[i][j - 2].locked = True
    grid[i][j - 3].locked = True
    grid[i - 1][j - 3].locked = True
    grid[i - 2][j - 3].locked = True
    grid[i + 1][j - 1].locked = True
    grid[i + 2][j - 1].locked = True
    grid[i][j + 1].locked = True
    grid[i][j + 2].locked = True
    grid[i][j + 3].locked = True
    grid[i + 1][j + 1].locked = True
    grid[i + 2][j + 1].locked = True
    grid[i + 2][j + 2].locked = True
    grid[i + 2][j + 3].locked = True
    grid[i - 1][j + 3].locked = True
    grid[i - 2][j + 3].locked = True
    grid[i - 2][j + 2].locked = True
    grid[i - 2][j + 1].locked = True

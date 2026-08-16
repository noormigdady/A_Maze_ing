def lock_42(grid, heigh, width):
    locked = []
    if width < 11 or height < 9:
        return []
    i = height // 2
    j = width // 2
    locked.append(grid[i][j - 1])
    locked.append(grid[i][j - 2])
    locked.append(grid[i][j - 3])
    locked.append(grid[i - 1][j - 3])
    locked.append(grid[i - 2][j - 3])
    locked.append(grid[i + 1][j - 1])
    locked.append(grid[i + 2][j - 1])
    locked.append(grid[i][j + 1])
    locked.append(grid[i][j + 2])
    locked.append(grid[i][j + 3])
    locked.append(grid[i + 1][j + 1])
    locked.append(grid[i + 2][j + 1])
    locked.append(grid[i + 2][j + 2])
    locked.append(grid[i + 2][j + 3])
    locked.append(grid[i - 1][j + 3])
    locked.append(grid[i - 2][j + 3])
    locked.append(grid[i - 2][j + 2])
    locked.append(grid[i - 2][j + 1])
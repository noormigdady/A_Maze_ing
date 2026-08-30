def print_maze(maze, height, width, entry, Exit, show_path, colors, path):
    maze_color = colors["maze_color"]
    color_42 = colors["color_42"]
    rows = height * 2 + 1
    print(maze_color + "█", end="")
    for j in range(width):
        print(maze_color + "████", end="")
    print()
    for row in range(1, rows - 1):
        i = (row - 1) // 2
        print(maze_color + "█", end="")
        for j in range(width):
            if maze[i][j].locked:
                color = color_42
            else:
                color = maze_color
            if row % 2 == 0:
                if maze[i][j].bottom:
                    print(color + "████", end="")
                else:
                    print(color + "   █", end="")
            else:
                if maze[i][j].locked:
                    print(color + "████", end="")
                elif maze[i][j].right:
                    print(color + "   █", end="")
                else:
                    print(color + "    ", end="")
        print()

    print(maze_color + "█", end="")
    for j in range(width):
        print(maze_color + "████", end="")
    print("\033[37m")

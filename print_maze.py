import os
BLUE = "\033[34m"
RESET = "\033[0m"


def print_maze(maze, height, width):

    # Top border
    os.system("")
    print(BLUE + "┌" + "───┬" * (width - 1) + "───┐" + RESET)

    for row in range(height):

        # Cell contents
        print(BLUE + "│", end="")

        for col in range(width):

            print("   ", end="")

            if maze[row][col].right:
                print("│", end="")
            else:
                print(" ", end="")

        print(BLUE + RESET)

        # Walls between rows
        if row < height - 1:

            print(BLUE + "├", end="")

            for col in range(width):

                if maze[row][col].bottom:
                    print("───", end="")
                else:
                    print("   ", end="")

                if col < width - 1:
                    print("┼", end="")

            print("┤" + RESET)

    # Bottom border
    print(BLUE + "└" + "───┴" * (width - 1) + "───┘" + RESET)

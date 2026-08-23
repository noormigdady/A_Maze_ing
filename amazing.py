import sys
import random
from generator import MazeGenerator
from lock_42 import lock_42
from print_block import print_maze
from config_parser import config_parser
from find_path import find_path



def menu():
    print("\n=== A-Maze-ing ===")
    print("1. Re-generate a new maze")
    print("2. Show/Hide path from entry to exit")
    print("3. Rotate maze colors")
    print("4. Quit")


def shuffle_colors():
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    COLORS = [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
    maze_color = random.choice(COLORS)
    color_42 = random.choice(COLORS)
    return {"maze_color": maze_color, "color_42": color_42}

def imperfecter(maze, height, width):
    pass

def produce(file, num):
    show_path = False
    path = None
    colors = {
            "maze_color": "\033[31m",
            "color_42": "\033[37m"
            }
    if num == 2:
        show_path = True
    if num == 3:
        colors = shuffle_colors()
    config = config_parser(file)
    width = config["WIDTH"]
    height = config["HEIGHT"]
    entry = config["ENTRY"]
    Exit = config["EXIT"]
    perfect = config["PERFECT"]
    grid = MazeGenerator(height, width)
    lock_42(grid.grid, height , width)
    maze = grid.generator(entry)
    if show_path:
        path = find_path(maze, height, width, entry, Exit, grid.sequence)
    if not perfect:
        imperfecter(maze, height, width)
    print_maze(maze, height, width, entry, Exit, show_path, colors, path)
    menu()

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage:  python3 amazing.py config.txt")
        return
    try:
        with open(args[1], "r") as f:
            pass 
    except FileNotFoundError as e:
        print(e)

    produce(args[1], 0)
    while True:
        try:
            num = int(input("Choice? (1-4):"))
            if num not in [1, 2, 3, 4]:
                continue
            if num == 4:
                print("Quitting the program !!")
                break
            produce(args[1], num)
        except Exception as e:
            message = str(e).split(",")
            print(message[0])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting the program !!")

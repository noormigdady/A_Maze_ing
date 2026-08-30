class Node:
    def __init__(self, cord):
        self.cord = cord
        self.next = None
class Queue:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

def get_open_walls(cell):
    opens = []
    if not cell.top:
        opens.append("top")
    if not cell.bottom:
        opens.append("bottom")
    if not cell.right:
        opens.append("right")
    if not cell.left:
        opens.append("left")
    return opens
paths = {

        }
def Next_cell(direction, maze, cell):
    i = cell.i
    j = cell.j
    if direction == "top":
        i -= 1
    if direction == "bottom":
        i += 1
    if direction == "right":
        j += 1
    if direction == "left":
        j -= 1
    return maze[i][j]
def adjust(Queue, Node):
    Queue.tail.next = Node
    Node.next = None

def find_path(maze, Entry, Exit):
    i, j = Entry
    x, y = Exit
    cell = maze[i][j]
    node = Node(Entry)
    queue = Queue(node, node)
    paths[entry] = queue
    while cell is not Exit:
        directions = get_open_walls(cell)
        if len(directions) == 1:
            next_cell = Next_cell(direction,maze, cell)
            node = Node(next_cell.i, next_cell.j)
            adjust(queue, node)
            cell = next_cell
        else:
            for direction in directions:
                next_cell = Next_cell(direction, maze, cell)




def main():
    find_path(0, 0, 0)
main()

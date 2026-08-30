class Node:
    def __init__(self, cord):
        self.cord = cord
        self.next = None
class Queue:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

def main():
    node = Node((1,2))
    queue = Queue(node, node)
    print(id(node))
    print(id(queue.head))
    print(id(queue.tail))
    print("\n\n\n\n\n")
    print(id(node.next))
    print(id(queue.head.next))
    print(id(queue.tail.next))
main()

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Step 1: Link new node to current head

        if self.head is not None:
            self.head.prev = new_node  # Step 2: Update old head's prev pointer

        self.head = new_node  # Step 3: Move head to new node

    # Print list forward
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage
dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)

dll.print_list()  # Output: 30 20 10
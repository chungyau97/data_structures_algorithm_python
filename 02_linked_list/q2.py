import linked_list

class Node(linked_list.Node):
    def __init__(self, data, next, prev) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList(linked_list.LinkedList):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_forward(self):
        self.print()
    
    def insert_at_begining(self, data):
        self.head = Node(data, self.head, None)

    def insert_at_end(self, data):
        if self.is_empty() == True:
            self.insert_at_begining(data)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(data, None, node)
        self.tail = node.next

    def print_backward(self):
        if self.is_empty(True) == True:
            return
        
        node = self.tail
        node_str = ''
        while node:
            node_str += str(node.data) + ' --> '
            node = node.prev
        print(node_str)


linked_list = LinkedList()
linked_list.print()
linked_list.insert_values(["banana","mango","grapes","orange"])
linked_list.print_forward()
linked_list.print_backward()
class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def is_empty(self, do_print = False):
        is_empty = self.head is None

        if is_empty == True and do_print == True:
            print('Linked List is empty.')
        
        return is_empty

    def insert_at_end(self, data):
        if self.is_empty() == True:
            self.insert_at_begining(data)
            return
        
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data, None)
    
    def print(self):
        if self.is_empty(True) == True:
            return
        
        node = self.head
        node_str = ''
        while node:
            node_str += str(node.data) + ' --> '
            node = node.next
        print(node_str)

    def insert_values(self, values):
        for value in values:
            self.insert_at_end(value)

    def get_length(self):
        count = 0

        node = self.head
        while node:
            count += 1
            node = node.next
        
        return count

    def __verify_index(self, index):
        node_length = self.get_length() - 1

        return index < 0 or index > node_length

    def insert_at(self, index, data):
        if self.__verify_index(index) == True:
            print('Invalid index position')
            return
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        node = self.head
        while node:
            if count == index - 1:
                node.next = Node(data, node.next)
                return
            
            node = node.next
            count += 1

    def remove_at(self, index):
        if self.__verify_index(index) == True:
            print('Invalid index position')
            return
        
        if index == 0:
            node = self.head
            self.head = node.next
            return
        
        count = 0
        node = self.head
        while node:
            if count == index - 1:
                node.next = node.next.next
                return
            
            node = node.next
            count += 1

# linked_list = LinkedList()
# linked_list.print()
# linked_list.insert_values(["banana","mango","grapes","orange"])
# linked_list.print()
# linked_list.insert_at(-1, 'pineapple')
# linked_list.insert_at(3, 'pineapple')
# linked_list.print()
# linked_list.remove_at(3)
# linked_list.print()
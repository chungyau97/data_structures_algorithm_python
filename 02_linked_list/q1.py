import linked_list

Node = linked_list.Node

class LinkedList(linked_list.LinkedList):

    def insert_after_value(self, data_after, data_to_insert):
        if self.is_empty(True):
            return

        node = self.head
        while node:
            if node.data == data_after:
                node.next = Node(data_to_insert, node.next)
                return
            
            node = node.next

        print('data_after is not found in linked list.')

    def remove_by_value(self, data_to_remove):
        if self.is_empty(True):
            return
        
        if self.head.data == data_to_remove:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.data == data_to_remove:
                node.next = node.next.next
                return
            
            node = node.next
        
        print('data_to_remove is not found in linked list.')

linked_list = LinkedList()
linked_list.insert_values(["banana","mango","grapes","orange"])
linked_list.print()
linked_list.insert_after_value("mango","apple") # insert apple after mango
linked_list.print()
linked_list.remove_by_value("orange") # remove orange from linked list
linked_list.print()
linked_list.remove_by_value("figs")
linked_list.print()
linked_list.remove_by_value("banana")
linked_list.remove_by_value("mango")
linked_list.remove_by_value("apple")
linked_list.remove_by_value("grapes")
linked_list.print()
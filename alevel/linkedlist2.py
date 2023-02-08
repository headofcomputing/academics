class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_item(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_item(self, key):
        prev = None
        temp = self.head
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next
        del temp

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")
linked_list = LinkedList()
linked_list.insert_item(1)
linked_list.insert_item(2)
linked_list.insert_item(3)
linked_list.insert_item(4)
linked_list.print_list()
linked_list.delete_item(3)
linked_list.print_list()

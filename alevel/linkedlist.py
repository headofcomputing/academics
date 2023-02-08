# a program to implement linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    def delete(self, data):
        temp = self.head
        if temp.data == data:
            self.head = temp.next
        else:
            while temp.next is not None:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next
    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False
linkedList=[Node(1,1),Node(2,2),Node(3,3),Node(4,4),Node(5,5),Node(6,6),Node(7,7),Node(8,8),Node(9,9),Node(10,10)]
startPointer=0
emptyList=[]  

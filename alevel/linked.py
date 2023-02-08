class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
link=LinkedList()
elem=Node(1)
link.head=elem
link.show()
elem2=Node(2)
link.head.next=elem2
link.show()
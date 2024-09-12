class Node:
    def __init__(self, val) :
        self.item = val
        self.next = None

class SLList:
    def __init__(self):
        self.front = None
        self.counter = 0

    def tambah(self, newval):
        # create a new temporary node
        # before being inserted into the linked list
        tempnode = Node(newval)

        # insert the temporary node into  
        # the beginning of the list
        temp_ptr = self.front
        self.front = tempnode
        self.front.next = temp_ptr

        # increase the count of the list's elements
        self.counter += 1

        temp = self.front
        # go to the last node of the linked list
        for x in range(self.counter-1):
            temp = temp.next
        temp.next = self.front

        return self.counter



llist = SLList()
x = llist.tambah("Node 1")
x = llist.tambah("Node 2")
x = llist.tambah("Node 3")
x = llist.tambah("Node 4")
x = llist.tambah("Node 5")

temp = llist.front
for i in range(x):
    print(temp.item, end = " ")
    print('--> '+temp.next.item)
    temp = temp.next


class Node:
    def __init__(self, val) :
        self.item = val
        self.next = None

class SLList:
    def __init__(self, max):
        self.front = None
        self.counter = 0

    def tambah(self, newval):
        tempnode = Node(newval)
        tempnode.next = self.front
        self.front = tempnode

        self.counter += 1
        return self.counter
    
    def tambahBlkg(self, newval):
        tempnode = Node(newval)
        temp = self.front
        for i in range(self.counter-1):
            temp = temp.next
        temp.next = tempnode
        self.counter += 1
        return self.counter

llist = SLList(4)
x = llist.tambah("Node 1")
x = llist.tambah("Node 2")
x = llist.tambahBlkg("Node 3")
x = llist.tambah("Node 4")
x = llist.tambah("Node 5")


temp = llist.front
for i in range(x):
    print(temp.item,end=" ")
    if (temp.next != None):
        print('--> '+temp.next.item)
    else:
        print('--> None')
    temp = temp.next


# llist.counter = x




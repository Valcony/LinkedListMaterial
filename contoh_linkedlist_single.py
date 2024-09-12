class Node:
    def __init__(self, val) :
        self.item = val
        self.next = None

class SLList:
    def __init__(self):
        self.front = None


llist = SLList()
n1 = Node("Satu")
n2 = Node("Dua")
n3 = Node("Tiga")
n4 = Node("Empat")
n5 = Node("Lima")

llist.front = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = llist.front

temp = llist.front # alias dari n1
for x in range(4):
    print(temp.item) # n1.item
    temp = temp.next # temp=n1.next
                      # temp=n2


print("======= Add at the beginning =======")

n_new = Node("Baru")
llist.front = n_new
llist.front.next = n1 # n_new.next = n1

temp = llist.front
for x in range(5):
    print(temp.item)
    temp = temp.next



print("=========== INSERT ================")

n_insert = Node("insert")
temp = llist.front
for x in range(2):
    temp = temp.next
old_next = temp.next
temp.next = n_insert
n_insert.next = old_next

temp = llist.front
for x in range(6):
    print(temp.item)
    temp = temp.next

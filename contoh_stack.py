class Node:
    def __init__(self, val) :
        self.item = val
        self.next = None

class Stack:
    def __init__(self, max):
        self.front = None
        self.counter = 0
        self.max = max

    def push(self, newval):
        if self.counter < self.max:
            tempnode = Node(newval)
            tempnode.next = self.front
            self.front = tempnode

            self.counter += 1
        return self.counter

    def pop(self):
        infopop = None
        if self.counter > 0:
            stacktemp = self.front.next
            infopop = self.front.item
            self.front = stacktemp
            self.counter -= 1
        return infopop

    def isNull(self):
        if self.counter == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.counter >= self.max:
            return True
        else:
            return False



stack = Stack(3)  # Buat stack yang hanya bisa menyimpan 3 data

# Isi stack dengan 3 nilai berbeda
x = stack.push(27)
x = stack.push(145)
x = stack.push(66)

if stack.isFull:
    print('Stack sudah penuh')

# Tambah isi stack
x = stack.push(87)  # angka 87 tidak akan tersimpan karena stack sudah terisi 3 data

nilaihapus = stack.pop()
print('Stack sudah dikurangi 1 baris.')
print('Baris yang terbuang:' + str(nilaihapus))

# Tambah isi stack
x = stack.push(38)  

# tampilkan seluruh isi stack
temp = stack.front
for i in range(x):
    print('Node: ' + str(temp.item))
    temp = temp.next



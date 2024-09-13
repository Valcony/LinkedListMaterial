class Node:
    def __init__(self, value):
        # value node tsb = String
        # Atribut reference next node -> nnti next = object Node
        self.item = value
        self.next = None

class SingleLinked:
    def __init__(self, max):
        # Front reference to 1st Node
        # Counter gunanya buat pengecekan length dlm list
        self.front = None
        self.counter = 0

        # Goal:
        # Buat tampilan ✓
        # Buat add di depan ✓, belakang ✓, dan index tertentu ✓
        # [ada dua cara, yg di temp Node baru / yg di temp Node yg mau diubah]
        # Buat hapus pada depan ✓, belakang ✓, dan index tertentu ✓ 

    def show(self):
        temp  = self.front
        for i in range(self.counter):
            # Klo i ga punya next brarti next  = none
            print(temp.item, end="")
            if (temp.next != None):
                print(" ----> "+temp.next.item)
            else:
                print(" ----> None")
            temp = temp.next
        # Klo ga pake counter
        # temp = self.head
        # while temp.next != None:
        #   print(temp.data, "---> ", end="")
        #   temp = temp.next
        # print(temp.data)
    
    def addFront(self, newValue):
        # Summary
        # Bkin temp buat Node baru
        # Front jadi Node baru, Nextnya Node baru = Front lama
        # Add counter, return counter
        temp = self.front
        self.front = Node(newValue)
        self.front.next = temp
        self.counter+=1
        return self.counter
    
    def addIndex(self, index, newValue):
        # Summary
        # Buat iterasi sampe index yg dimau -1 (karena mau akses nextnya Node sebelum index Node baru)
        # Buat temp untuk Node di posisi index yg mau ditambahkan (supaya nanti digeser)
        # Buat Node pada posisi yg dimau jadi Node baru
        # Buat nextnya Node baru jadi Node lama yg di temp tadi
        # Add Counter, return counter
        # <--- Klo index =  0 artinya dia lgsg front, jadi lgsg call function addFront aja --->

        tempIteration = self.front
        if index == 0:
            self.addFront(newValue)
        elif index == self.counter-1:
            self.addBack(newValue)
        else:
            # Akses Node yang sebelum dimau supaya Nextnya dibikin Node yang baru
            # index = Berapa kali dibutuhin ke index yg dimau - front (1) 
            for i in range(index-1):
                tempIteration = tempIteration.next
                # Buat yg dimau jadi temp
            tempNode = tempIteration.next
            # Buat yang dimau jadi Node value Baru
            tempIteration.next = Node(newValue)
            # Buat nextnya node Baru jadi tempNode
            tempIteration.next.next = tempNode
            self.counter+=1
        
        return self.counter
        
    
    def addBack(self, newValue):
        # Summary
        # Temp Node baru
        # Bkin iterasi dari front to back
        # Nextnya back = Node baru
        # Add Counter, return counter
        tempNode = Node(newValue)
        tempIteration = self.front
        for i in range(self.counter-1):
            tempIteration = tempIteration.next
        tempIteration.next = tempNode
        # Klo gapake Counter
        #  while(temp.next != None):
            # temp = temp.next
        # temp.next = Node(data)
        self.counter += 1
        return self.counter
    
    def delFront(self):
        # Summary
        # Set Frontnya list jadi Nextnya Front awal List
        # Kurangi Counter, return counter
        self.front = self.front.next
        self.counter -= 1
        return self.counter
    
    def delIndex(self, index):
        # Summary
        # Buat iterasi sampe index yang dimau buat store nextnya yg mau dihapus, temp Node next tsb
        # Buat iterasi ulang dari front sampe index-1 yang dimau supaya ngubah next sebelum Node yg dihapus jadi temp tadi
        # Kurangi Counter, return Counter
        if index == 0:
            self.delFront()
        elif index == self.counter-1:
            self.delBack()
        else:
            tempIteration = self.front
            for i in range(index):
                    tempIteration = tempIteration.next
            tempNode = tempIteration.next
            tempIteration = self.front
            for i in range(index-1):
                tempIteration = tempIteration.next
            tempIteration.next = tempNode
            self.counter -=1
        return self.counter
    
    def delBack(self):
        tempIteration = self.front
        # Buat Node -1 paling akhir, nextnya dibuat None
        # Range = counter - 2 karena mau akses -1 paling akhir, jadi length kurangi front & back
        # Kurangi Counter, return counter
        for i in range(self.counter-2):
            tempIteration = tempIteration.next
        tempIteration.next = None
        self.counter -= 1
        return self.counter

        
    

list = SingleLinked(0)
x = list.addFront("Node 1")
x = list.addFront("Node 3")
x = list.addBack("Node 9")
x = list.addFront("Node 2")
# x = list.addIndex(1, "Node 8")
x = list.delIndex(2)

list.show()
print(list.counter)

# Notes:
# Klo yg ga berhubungan lgsg sama front (di index tertentu/back),
# Loop sampe index di posisi -1 sebelum yg dimau buat ngedit nextnya Node sebelumnya

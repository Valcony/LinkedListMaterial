class Node:
    def __init__(self, value):
        # value node tsb = String
        # Atribut reference next node -> nnti next = object Node
        self.item = value
        self.next = None
        self.prev = None

class DoubleLinked:
    def __init__(self, max):
        # Front reference to 1st Node
        # Counter gunanya buat pengecekan length dlm list
        self.front = None
        self.counter = 0
        self.back = None

        # Goal:
        # Buat tampilan ✓
        # Buat add di depan ✓, belakang ✓, dan index tertentu
        # [ada dua cara, yg di temp Node baru / yg di temp Node yg mau diubah]
        # Buat hapus pada depan ✓, belakang ✓, dan index tertentu

    def show(self):
        temp  = self.front
        for i in range(self.counter):
            if (temp.prev != None):
                print(temp.prev.item +" <---- ", end="")
            else:
                print("None <---- ", end="")
            # Klo i ga punya next brarti next  = none
            print(temp.item, end="")
            if (temp.next != None):
                print(" ----> "+temp.next.item)
            else:
                print(" ----> None")
            temp = temp.next
    
    def addFront(self, newValue):
        # Summary
        # Bkin temp buat Node baru, nextnya Node baru = Front lama
        # Klo list ada isinya, prevnya Front lama diisi Node baru yg di temp
        # Klo gaada isinya, bkin back nya list jadi Node baru yg di temp (soalnya gaad elemen lain)
        # Front jadi Node baru
        # Add counter, return counter
        temp = Node(newValue)
        temp.next = self.front
        if self.counter != 0:
            self.front.prev = temp
        else:
            self.back = temp
        self.front = temp
        self.counter+=1
        
        return self.counter
    
    def addIndex(self, index, newValue):
        # BLMMMMM
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
            for i in range(index-2):
                tempIteration = tempIteration.next
                # Buat yg dimau jadi temp
            
            # tempNode = tempIteration.next
            # # Buat yang dimau jadi Node value Baru
            # tempIteration.next = Node(newValue)
            # tempIteration.next.prev =  tempIteration
            # # Buat nextnya node Baru jadi tempNode
            # tempIteration.next.next = tempNode
            self.counter+=1
        
        return self.counter
        
    
    def addBack(self, newValue):
        # Summary
        # Temp Node baru
        # Bkin iterasi dari front to back
        # Prevnya Node baru = akhir
        # Nextnya akhir = Node baru
        # Add Counter, return counter
        tempNode = Node(newValue)
        tempIteration = self.front
        for i in range(self.counter-1):
            tempIteration = tempIteration.next
        tempNode.prev = tempIteration
        tempIteration.next = tempNode
        
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
        # BLMMMMMM
        if index == 0:
            self.delFront()
        elif index == self.counter-1:
            self.delBack()
        else:
            tempIteration = self.front
            for i in range(index-1):
                tempIteration = tempIteration.next
            # tempNode = tempIteration.next
            # tempIteration.next = tempNode.next
            tempIteration.next.next
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

        
    

list = DoubleLinked(0)
x = list.addFront("Node 1")
x = list.addFront("Node 3")
x = list.addBack("Node 9")
# x = list.addFront("Node 2")
# x = list.addIndex(1, "Node 9")
# x = list.delIndex(2)

list.show()

# Notes:
# Klo yg ga berhubungan lgsg sama front (di index tertentu/back),
# Loop sampe index di posisi -1 sebelum yg dimau buat ngedit nextnya Node sebelumnya
# Double Fron & Back sama utk delete

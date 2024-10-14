class Node:
    def __init__(self, value):
        # value node tsb = String
        # Atribut reference next node -> nnti next = object Node
        self.item = value
        self.next = None
        self.prev = None

class DoubleLinked:
    def __init__(self):
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
        # Summary
        # Buat iterasi sampe index yg dimau, setor Node yang di index jadi temp
        # Buat new Node, isi nextnya dari temp yang dibuat tadi
        # Buat iterasi sampe index-1 yg dimau buat ubah next dari Node sblm index yg ditambah
        # Ubah prevnya Node baru & nextnya Node index-1
        # Add Counter, return Counter
        # <--- Klo index =  0 artinya dia lgsg front, jadi lgsg call function addFront aja --->

        tempIteration = self.front
        if index == 0:
            self.addFront(newValue)
        elif index == self.counter-1:
            self.addBack(newValue)
        else:
            # Akses index yang dimau jadi temp n, ubah previous e jadi Node baru
            for i in range(index):
                tempIteration = tempIteration.next
            # Buat new Node, isi next baru prevnya
            tempNode = Node(newValue)
            tempNode.next = tempIteration
            tempIteration.prev = tempNode
            # Akses index sebelum yang dimau supaya ubah nextnya jadi temp
            tempIteration = self.front
            for i in range(index-1):
                tempIteration = tempIteration.next
            tempNode.prev = tempIteration
            tempIteration.next = tempNode
            self.counter+=1
        
        return self.counter
        
    
    def addBack(self, newValue):
        # Summary
        # Temp Node baru
        # Bkin iterasi dari front to back (akhir)
        # Prevnya Node baru = Node akhir yg lama
        # Nextnya Node akhir yg lama = Node baru
        # Add Counter, return counter

        tempNode = Node(newValue)
        tempIteration = self.front
        for i in range(self.counter-1):
            tempIteration = tempIteration.next
        tempNode.prev = tempIteration
        tempIteration.next = tempNode
        self.back = tempNode
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
          nodeAfter = tempIteration.next
          nodeBefore = tempIteration.prev
          if nodeAfter != None:
            nodeAfter.prev = nodeBefore
          if nodeBefore != None:
            nodeBefore.next = nodeAfter

          # Cara lain
            # tempIteration = self.front
            # for i in range(index):
            #         tempIteration = tempIteration.next
            # tempNode = tempIteration.next

            # tempIteration = self.front
            # for i in range(index-1):
            #     tempIteration = tempIteration.next
            # tempIteration.next = tempNode
            # tempNode.prev = tempIteration
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

    def reverse(self):
      temp = self.back
      while temp.prev != None:
        if temp.next != None:
          print(temp.next.item, "<---", end=" ")
        else:
          print("None <---", end=" ")
        print(temp.item, "--->", temp.prev.item, end=" ")
        temp = temp.prev
        print()
      print(self.front.next.item, "<---", end=" ")
      print(self.front.item, "---> None")

        
    

list = DoubleLinked()
x = list.addFront("Node 1")
x = list.addFront("Node 3")
x = list.addBack("Node 9")
# x = list.addFront("Node 2")
x = list.addIndex(1, "Node 5")
x = list.delIndex(2)
x = list.reverse()

# list.show()


# Notes:
# Klo yg ga berhubungan lgsg sama front (di index tertentu/back),
# Loop sampe index di posisi -1 sebelum yg dimau buat ngedit nextnya Node sebelumnya
# Double front, index, back, sama utk delete

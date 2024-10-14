import datetime

class Node:
    def __init__(self, val, thn, bln, tgl) :
        self.item = val
        self.date = datetime.date(thn, bln, tgl)
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.counter = 0


    # ----------------------------------------------------
    # Menambah node baru di posisi paling belakang
    # ----------------------------------------------------
    def enqueue(self, newval, thn, bln, tgl):
        newNode = Node(newval, thn, bln, tgl)

        newNode.prev = self.back
        if (self.counter != 0):
            self.back.next = newNode
        else:
            self.front = newNode
        self.back = newNode

        self.counter += 1
        return self.counter


    # ----------------------------------------------------
    # Hapus node pada posisi tertentu
    # untuk queue, selalu posisi paling awal yang berindex 1
    # ----------------------------------------------------
    def dequeue(self, index=1):
        temp_ptr = self.front

        # kalau yg dihapus adalah node pertama,
        # ubah pointer front menuju node kedua
        if index == 1:
            self.front = temp_ptr.next
        # kalau tidak, lompat ke posisi yg dituju 
        else:
            for i in range(index-1):
                temp_ptr = temp_ptr.next
        
        node_after  = temp_ptr.next
        node_before = temp_ptr.prev
        if node_after != None:
            node_after.prev = node_before
        if node_before != None:
            node_before.next = node_after

        self.counter = self.counter - 1


    # ----------------------------------------------------
    # Tampilkan seluruh node di dalam list
    # ----------------------------------------------------
    def tampil(self):
        temp = self.front
        print('--------------------------------------')

        for i in range(self.counter):
            # Tampilkan pointer prev
            if temp.prev != None:  print(temp.prev.item,'<--| ',end="")
            else:  print('  None <--| ',end="")

            # Tampilkan nama node
            print(temp.item, temp.date, end="")

            # Tampilkan pointer next
            if temp.next != None:  print(' |--> '+temp.next.item)
            else:  print(' |--> None')

            temp = temp.next
            print('--------------------------------------')


    # ----------------------------------------------------
    # Hapus elemen queue yang sudah expired
    # ----------------------------------------------------
    def hapusExpired(self,ExpDate):
        # Buat fungsi untuk menghapus isi queue yang date <= ExpDate
        return False


def SetExpiryDate(jml):
    return HariIni + datetime.timedelta(days=jml)



q = Queue()
x = q.enqueue("Indomie",2024,9,26)
x = q.enqueue("Samyang",2024,9,28)
x = q.enqueue("Momofuku",2024,10,3)
x = q.enqueue("Ichiran",2024,10,6)
x = q.enqueue("Nongshim 5",2024,10,15)
q.tampil()

print('==============================================================')
q.dequeue()
q.tampil()

print('==============================================================')

HariIni = datetime.date(2024,9,26)  # set tanggal hari ini 26 Sept 2024
ExpiryDate = SetExpiryDate(6)       # set expiry date = 6 hari setelah 26 Sept 2024
print("Expiry Date = ",ExpiryDate)

q.hapusExpired(ExpiryDate)
q.tampil()

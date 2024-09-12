class Node:
    def __init__(self, val) :
        self.item = val;
        self.next = None;
        self.prev = None;

class DLList:
    def __init__(self):
        self.front = None;
        self.back = None;
        self.counter = 0;


    # ----------------------------------------------------
    # Tampilkan seluruh node di dalam list
    # ----------------------------------------------------
    def tampil(self):
        temp = self.front;
        print('--------------------------------------');

        for i in range(self.counter):
            # Tampilkan pointer prev
            if temp.prev != None:  print(temp.prev.item,'<--| ',end="");
            else:  print('  None <--| ',end="");

            # Tampilkan nama node 
            print(temp.item,end="");

            # Tampilkan pointer next
            if temp.next != None:  print(' |--> '+temp.next.item);
            else:  print(' |--> None');

            temp = temp.next;
            print('--------------------------------------');



    # ----------------------------------------------------
    # Menambah node baru di posisi paling depan
    # ----------------------------------------------------
    def tambah_depan(self, newval):
        newNode = Node(newval);

        newNode.next = self.front
        if (self.counter != 0):
            self.front.prev = newNode
        else:
            self.back = newNode
        self.front = newNode

        self.counter += 1;
        return self.counter   

    # ----------------------------------------------------
    # Menambah node baru di posisi paling belakang
    # ----------------------------------------------------
    def tambah_blkng(self, newval):
        newNode = Node(newval);

        newNode.prev = self.back
        if (self.counter != 0):
            self.back.next = newNode
        else:
            self.front = newNode
        self.back = newNode

        self.counter += 1;
        return self.counter


    # ----------------------------------------------------
    # Hapus node pada posisi tertentu
    # posisi paling awal berindex 1
    # ----------------------------------------------------
    def hapus(self, index):
        temp_ptr = self.front;

        # kalau yg dihapus adalah node pertama,
        # ubah pointer front menuju node kedua
        if index == 1:
            self.front = temp_ptr.next;
        # kalau tidak, lompat ke posisi yg dituju 
        else:
            for i in range(index-1):
                temp_ptr = temp_ptr.next;
        
        node_after  = temp_ptr.next;
        node_before = temp_ptr.prev;
        if node_after != None:
            node_after.prev = node_before;
        if node_before != None:
            node_before.next = node_after;

        self.counter = self.counter - 1;



list = DLList();
x = list.tambah_blkng("Node 1");
x = list.tambah_blkng("Node 2");
x = list.tambah_blkng("Node 3");
x = list.tambah_blkng("Node 4");
x = list.tambah_blkng("Node 5");

list.tampil();

print('===============================')

list.hapus(5);

list.tampil();
#===LATIHAN 3 (IMPLEMENTASIKAN PENCARIANPADA NODE TERTENTU DOUBLE LINKED LIST)===#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Menyimpan node terakhir untuk traversing mundur

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False    
        
dll = DoublyLinkedList()

#input elemen 
data_input = input("masukkan elemen ke dalam doubly linked list (pisahkan dengan koma): ")
data_list = data_input.split(",")

for item in data_list:
    dll.insert_at_end(int(item.strip()))

#input pencarian 
cari = int(input("masukkan elemen yang ingin dicari: "))

#proses pencarian
if dll.search(cari):
    print(f"elemen {cari} ditemukan dalam doubly linked list")
else:
    print(f"elemen {cari} tidak ditemuka dalam doubly linked list")    
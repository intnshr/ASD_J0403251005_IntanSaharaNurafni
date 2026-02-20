#===============================================================
#Nama : Intan Sahara Nurafni
#NIM  : J0403251005
#Kelas : TPL A2
#===============================================================


#===============================================================
#Implementasi Dasar : queueLL
#===============================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil / diinstansiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

class queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None 
    
    #membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self, data): 
        nodeBaru = Node(data) 

        #jika queue kosong, front dan rear menunjuk ke node baru
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return  

        #jika queue tidak kosong, maka letakan data baru ke setelah rear, dan jadikan data baru sebagai rear   
        self.rear.next = nodeBaru #letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #jadikan data baru sebagai rear 

    def deaqueue(self):
        #menghapus data dari depan / front
        data_terhapus = self.front.data #lihat data paling depan

        #geser front ke node barikutnya
        self.front = self.front.next

        #jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None 
    
    def tampilkan(self):
        current = self.front 
        print("Front -> " , end="")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print(" Rear ")

#Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.deaqueue()
q.tampilkan()
#===============================================================
#Nama : Intan Sahara Nurafni
#NIM  : J0403251005
#Kelas : TPL A2
#===============================================================


#===============================================================
#Implementasi Dasar : Stack
#===============================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil / diinstansiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#stack ada operasi push (memasukkan head baru) dan pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None #stack kosong jika top menunjuk ke none
    
    def push(self, data): #memasukkan data baru pada stack
        #1). Membuat node baru
        nodeBaru = Node(data) #instansiasi/ memanggil konstruktor pada class node

        #2)> Node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top 

        #3). geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): #mengambil atau menghapus node paling atas

        if self.is_empty():
            print("Stack Kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            print("Stack Kosong, tidak bisa peek")
            return None
        return self.top.data

    def tampilkan(self):
        current = self.top 
        print("Top " , end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instansiasi class stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())

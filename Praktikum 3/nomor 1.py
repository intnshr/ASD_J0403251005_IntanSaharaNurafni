#===LATIHAN 1 (IMPLEMENTASI FUNGSI UNTUK MENGHAPUS NODE DENGAN NILAI TERTENTU)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next :
            last = last.next
        last.next = new_node
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data !=key :
            prev = temp
            temp = temp.next
        if temp is None :
            return
        prev.next = temp.next
        temp = None
        
cll = LinkedList()

for x in [1, 11, 111, 1111, 11111] :
    cll.insert_at_end(x)
print("sebelum dihapus: ") 
cll.display()
cll.delete_node(111)

print("setelah dihapus: ")
cll.display()
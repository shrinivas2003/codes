class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newNode=Node(data)
        if(self.head):
            current=self.head
            while(current.next):
                current=current.next
            current.next=newNode
        else:
            self.head=newNode
    def iterate_item(self):
        current_item=self.head
        while current_item:
                val=current_item.next
                current_item=current_item.next
                yield val
LL=LinkedList()
LL.insert(9)
LL.insert(98)
LL.insert('welcome')
LL.insert(23)
LL.insert(5)
print("list: ")
for val in LL.iterate_item():
    print(val)
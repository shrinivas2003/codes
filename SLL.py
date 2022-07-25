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
    def searchList(self,value):
        position=0
        found=0
        if self.head is None:
            print("the linked list does not exist")
        else:
            temp_node=self.head
            while temp_node is not None:
                position=position+1
                if temp_node.data==value:
                    print("THe required vlaue was found at position:"+str(position))
                    found=1
                temp_node=temp_node.next
        if found==0:
            print("the required value does not exist in the list")
    def printLL(self):
        current=self.head
        while(current):
            print(current.data)
            current=current.next
    def atBeg(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
    def delEnd(self):
        if(self.head==None):
            return
        elif(self.head.next==None):
            self.head=None
            return
        else:
            temp_node=self.head
            while((temp_node.next).next is not None):
                temp_node=temp_node.next
            print('deleted item=',(temp_node.next).data)
            temp_node.next=None
        return
LL=LinkedList()
LL.insert(9)
LL.insert(98)
LL.insert('welcome')
LL.insert(23)
print("content of the list")
LL.printLL()
LL.searchList(98)
LL.atBeg(5)
print("contents of the list: ")
LL.printLL()
LL.delEnd()
LL.delEnd()
print("contents of the list:")
LL.printLL()            
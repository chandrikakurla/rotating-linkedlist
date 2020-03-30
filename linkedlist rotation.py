#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    #creating newnode and inserting into linkedlist
    def insert(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while(lastnode.next is not None):
            lastnode=lastnode.next
        lastnode.next=newnode
    #printing linkedlist elements
    def printllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkedlist is empty")
            return
        while(currentnode is not None):
            print(currentnode.data)
            currentnode=currentnode.next
    #function for rotating linkedlist
    def rotate_llist(self,n):
        if n==0:
            return
        count=1
        temp1=self.head
        current=self.head
        while(count<n and  current is not None):
            current=current.next
            count +=1
        
        self.head=current.next
        current.next=None
        temp2=self.head
        while(temp2.next is not None):
            temp2=temp2.next
        temp2.next=temp1

if __name__=="__main__":
    llist=LinkedList()
    for i in range(1,8):
        llist.insert(i)
    print("linkedlist before rotating")
    llist.printllist()
    n=int(input("enter rotation number:"))
    print(n)
    llist.rotate_llist(n)
    print("linked list after rotating %d steCps"%(n))
    llist.printllist()
    
   

# insert a node at middle of the linked list
# not show correct answer
class Node:
    def __init__(self,datavalues):
        self.datavalues=datavalues
        self.next=None
class s_linkedlist:
    def __init__(self):
        self.head=None
    def printLL(self):
        printval=self.head
        while printval is not None:
            print(printval.datavalues)
            printval=printval.next
    def insert_at_middle(self,newnode,position):
        Newnode=Node(newnode)
        if self.head is None:
            self.head=Newnode
            return
        i=0
        temp=self.head
        while(i<position):
            temp=temp.next
            i+=1
        Newnode.next=temp.next
        temp.next=Newnode
        
list1=s_linkedlist()
list1.head=Node(1)
e2=Node(2)
e3=Node(4)
list1.head.next=e2
e2.next=e3
list1.printLL()
list1.insert_at_middle(Node(3),2)
list1.printLL()

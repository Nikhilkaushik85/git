# insert the node at last
class Node:
    def __init__(self,datavalue):
        self.datavalue=datavalue
        self.next=None
class s_linkedlist:
    def __init__(self):
        self.head=None
    def print1(self):
        printvalue=self.head
        while printvalue is not None:
            print(printvalue.datavalue)
            printvalue=printvalue.next
    def insert_at_last(self,newnode):       
        Newnode=Node(newnode)
        if self.head is None:
            self.head=Newnode
            return
        temp=self.head
        while (temp.next):
            temp=temp.next
        temp.next=Newnode
list1=s_linkedlist()
list1.head=Node("mon")
e2=Node("tue")
e3=Node("wed")
e4=Node("thr")
list1.head.next=e2
e2.next=e3
e3.next=e4
list1.print1()
print("\n")
list1.insert_at_last("fri")
list1.print1()
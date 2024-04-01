# insert at bigining of linked list
class Node:
    def __init__(self,datavalue=None):
        self.datavalue=datavalue
        self.next=None
class slinked_list:
    def __init__(self):
        self.headvalue=None
    def print1(self):
        printvalue=self.headvalue
        while printvalue is not None:
            print(printvalue.datavalue)
            printvalue=printvalue.next
    def insert_at_bigin(self,newnode):
        Newnode=Node(newnode)
        Newnode.next=self.headvalue
        self.headvalue=Newnode
list1=slinked_list()
list1.headvalue=Node("mon")
e2=Node("tue")
e3=Node("wed")
list1.headvalue.next=e2
e2.next=e3
list1.print1()
print("again")
list1.insert_at_bigin("sun")
list1.print1()

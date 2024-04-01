# travesing the element
class Node:
    def __init__(self,datavalue=None):
        self.datavalue=datavalue
        self.next=None
class s_linkedlist:
    def __init__(self):
        self.headvalue=None
    def print1(self):
        printval=self.headvalue
        while printval is not None:
            print(printval.datavalue)
            printval=printval.next
list1=s_linkedlist()
list1.headvalue=Node("mon")
e2=Node("tue")
e3=Node("wed")
list1.headvalue.next=e2
e2.next=e3
list1.print1()

# 
# class Node:
#    def __init__(self, dataval=None):
#       self.dataval = dataval
#       self.nextval = None

# class SLinkedList:
#    def __init__(self):
#       self.headval = None

#    def listprint(self):
#       printval = self.headval
#       while printval is not None:
#          print (printval.dataval)
#          printval =printval.nextval

# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")

# # Link first Node to second node
# list.headval.nextval = e2

# # Link second Node to third node
# e2.nextval = e3

# list.listprint()
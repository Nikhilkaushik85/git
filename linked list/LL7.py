# delete a node from beginning
# not currect answer
class Node:
    def __init__(self,datavalue):
        self.datavalue=datavalue
        self.next=None
class s_linkedlist:
    def __init__(self):
        self.head=None
    def insert_node_begain(self,newnode):
        # temp=self.head
        Newnode=Node(newnode)
        Newnode.next=head
        head.next=Newnode
    def delete_from_first(self):
        if self.head is None:
            return
        else:
            temp=self.head
            head=self.head.next
            temp=None
    def printLL(self):
        temp=self.head
        while temp is not None:
            print(temp.datavalue)
            temp=temp.next
list1=s_linkedlist()
list1.head=Node("devesh")
e2=Node("dev")
e3=Node("sadela")
e4=Node("pilla")
list1.head.next=e2
e2.next=e3
e3.next=e4
list1.printLL()
print()
list1.delete_from_first()
list1.printLL()
# print()
# list1.delete_from_first()
# list1.printLL()
# print()
# list1.delete_from_first()
# list1.printLL()
# print()
# list1.delete_from_first()
# list1.printLL()


# delete a node using keyword
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class s_linked_list:
    def __init__(self):
        self.head=None
    def insert_node_at_first(self,newnode):
        Newnode=Node(newnode)
        Newnode.next=self.head
        head=Newnode
    def printLL(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def delete_Node(self,keyword):
        temp=self.head
        if self.head is not None:
            if (temp.data == keyword):
                self.head=self.head.next
                temp=None
                return
        while self.head is not None:
            if (temp.data==keyword):
                break
            prev=temp
            temp=temp.next
        if self.head==None:
            return 
        prev.next=temp.next
        temp=None

list1=s_linked_list()
list1.head=Node("nikhil")
e2=Node("nomesh")
e3=Node("head")
list1.head.next=e2
e2.next=e3
list1.printLL()
# list1.delete_Node('nomesh')
# print()
# list1.printLL()
list1.delete_Node('nikhil')
print()
list1.printLL()
list1.delete_Node('head')
print()
list1.printLL()
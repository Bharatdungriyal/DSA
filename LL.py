class Node:
    def __init__(self,value):
        self.data = value
        self.next= None
a= Node(1)
b= Node(2)
c= Node(3)
a.next = b
b.next = c

class Linked_list:
    def __init__(self):
        self.head = None
        self.n = 0 # number of nodes
    def __len__(self):
        return self.n

    def insert_head(self,value):
        new_Node = Node(value)
        new_Node.next = self.head
        self.head = new_Node
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]
    def append(self, value):
        new_Node = Node(value)
        if self.head== None:
            self.head = new_Node
            self.n += 1

        curr= self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_Node
        self.n += 1

    def insert_after(self,after,value):
        new_Node = Node(value)
        curr= self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            new_Node.next = curr.next
            curr.next = new_Node
            self.n += 1
        else:
            return "item not found "
    def clear(self):
        self.head= None
        self.n = 0

    def clear_head(self):
        if self.head== None:
            return "empty list"

        self.head= self.head.next
        self.n-= 1

    def pop(self):
        curr = self.head
        if curr.next == None:
            return self.clear_head()

        while curr.next.next != None:
            curr = curr.next
        curr.next= None
        self.n -=1

    def remove(self,value):
        curr = self.head
        if self.head == None:
            return "Empty LL"
        if self.head.data == value:
            return self.clear_head()

        while curr.next != None:
            if curr.next.data== value:
                break
            curr = curr.next
        if curr.next == None:
            return "not found"
        else:
            curr.next = curr.next.next
        self.n -=1

    def search(self,item):
        curr= self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return "not Found"



L = Linked_list()
L.insert_head(5)
L.insert_head(6)
L.insert_head(8)
L.insert_head(56)
L.insert_head(11)
L.insert_head(82)
L.insert_head(18)
L.insert_head(7)
L.append(100)
L.insert_after(6,200)
L.clear_head()
L.pop()
#L.clear()
L.remove(82)
print("the value is at index",L.search(56))
print(L)
print("no. of nodes ",len(L))
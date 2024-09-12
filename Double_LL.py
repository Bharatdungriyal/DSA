class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DOUBLE_LL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_end(self, data):
        temp = self.start
        if self.start is not None:
            while temp.next is not None:
                temp = temp.next
        n = Node(temp, data, None)
        if temp is None:
            self.start = n
        else:
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next  # This was missing
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()  # For a new line after printing the list

    def delete_item(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.start = temp.next
                break
            temp = temp.next

# Testing the code
LL = DOUBLE_LL()
LL.insert_at_start(2)
LL.insert_at_start(5)
LL.insert_at_start(8)
LL.insert_at_start(25)
LL.insert_at_start(12)
LL.insert_at_start(62)
LL.insert_after(LL.search(25),250)
LL.insert_at_end(100)
LL.print_list()  # Output: 62 12 25 8 5 2



class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(item=data)
        if self.is_empty():
            # If the list is empty, point the node to itself (circular)
            n.next = n
            n.prev = n
            self.start = n
        else:
            last = self.start.prev
            n.next = self.start
            n.prev = last
            last.next = n
            self.start.prev = n
            self.start = n

    def insert_at_end(self, data):
        n = Node(item=data)
        if self.is_empty():
            # If the list is empty, point the node to itself (circular)
            n.next = n
            n.prev = n
            self.start = n
        else:
            last = self.start.prev
            n.next = self.start
            n.prev = last
            last.next = n
            self.start.prev = n

    def search(self, data):
        if self.is_empty():
            return None

        temp = self.start
        while True:
            if temp.item == data:
                return temp
            temp = temp.next
            if temp == self.start:
                break
        return None

    def delete_item(self, data):
        if self.is_empty():
            return

        temp = self.start
        while True:
            if temp.item == data:
                if temp.next == temp:  # Only one element
                    self.start = None
                else:
                    prev_node = temp.prev
                    next_node = temp.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    if temp == self.start:
                        self.start = next_node
                break
            temp = temp.next
            if temp == self.start:
                break

    def print_list(self):
        if self.is_empty():
            print("List is empty")
            return

        temp = self.start
        while True:
            print(temp.item, end=" ")
            temp = temp.next
            if temp == self.start:
                break
        print()  # For a new line after printing the list

# Testing the Circular Doubly Linked List
CLL = CircularLinkedList()
CLL.insert_at_start(10)
CLL.insert_at_start(20)
CLL.insert_at_start(30)
CLL.insert_at_end(5)
CLL.insert_at_end(1)

CLL.print_list()  # Output: 30 20 10 5 1

# Deleting an element
CLL.delete_item(10)
CLL.print_list()  # Output: 30 20 5 1

# Searching for an element
found = CLL.search(5)
if found:
    print(f"Item {found.item} found!")  # Output: Item 5 found!
else:
    print("Item not found!")

import ctypes


class mylist:

    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)  # create a ctype array with size = self.size

    def __len__(self):
        return self.n

    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size * 2)

        self.A[self.n] = item
        self.n = self.n + 1
        # resize

    def __resize(self, New_capacity):
        B = self.__make_array(New_capacity)
        self.size = New_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign
        self.A = B
    def __getitem__(self, index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return "index error- index out of bound"
    def pop(self):        #PoP
        if self.n == 0:
            return "Empty list"
        print(self.n)
        self.n = self.n-1

    def clear(self): # clear
        self.size = 1
        self.n = 0
    def find(self,item):     # find
        for i in range(self.n):
            if self.A[i] == item:
                return f" it is at {i}"
        return 'Vale error'

    def insert (self,pos, item):   #insert
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        self.A[pos]= item
        self.n = self.n + 1

    def del_item(self,pos):       # del_item
        if 0<= pos< self.n:
            for i in range(pos,self.n-1):
               self.A[i]= self.A[i+1]
            self.n = self.n-1

    def remove(self, item): # remove
        pos = self.find(item)

        if type(pos)== int:
            self.del_item(pos)
        else:
            return pos




    def __str__(self):
        result = " "
        for i in range(self.n):
            result = result + str(self.A[i]) + ","
        return "["+ result[:-1]+"]"

    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()  # create a ctype array with size capacity


Lst = mylist()
print(len(Lst))
print(type(Lst))
Lst.append(3.14)
Lst.append(52.4)
Lst.append(4)
Lst.append("hello")
print(Lst)
print(type(Lst))
print(len(Lst))
print(Lst.__getitem__(1))
print(Lst)
print(Lst.find(52.4))
Lst.pop()
print(Lst)
Lst.pop()
print(Lst)
Lst.clear()
print(Lst)
Lst.append(2)
Lst.append(6)
Lst.append(8)
print(Lst)
Lst.insert(0,452)
Lst.insert(2,25)
Lst.insert(1, 278)
print(Lst)
Lst.del_item(1)
print(Lst)
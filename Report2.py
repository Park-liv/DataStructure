def Queue():
    queue = [None]*10
    i = 0
    while True:
        com = int(input("Input number: "))
        if com == 0:
            if queue[0] == None:
                print("Queue is empty.")
            else:
                for j in range(len(queue) - 1):
                    queue[j] = queue[j + 1]
                queue[j + 1] = None
                i -= 1
        elif com == -1:
            return #print(queue)
        else:
            if i >= len(queue):
                print("Queue is overflowed")
            else:
                queue[i] = com
                i += 1
        print(queue)    # 리스트 확인용
# Queue()

def Cqueue():
    queue = [None] * 10
    head = 0
    tail = 0
    while True:
        num = int(input("Input number: "))
        if num == 0:
            if queue[head] == None:
                print("Queue is empty")
            else:
                queue[head] = None
                head += 1
                if head >= len(queue):
                    head -= len(queue)
        elif num == -1:
            return #print(queue)
        else:
            if queue[tail] != None:
                print("Queue is overflowed")
            else:
                queue[tail] = num
                tail += 1
                if tail >= len(queue):
                    tail -= len(queue)
        print(queue)
Cqueue()

class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self): return self.size == 0

    def insert(self, item):
        if self.size == 10:
            print("Queue is overflowed")
        else:
            if self.is_empty():
                self.head = self.Node(item, None)
                self.tail = self.head
            else:
                p = self.Node(item, None)
                self.tail.next = p
                self.tail = p
            self.size += 1

    def delete(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.head = self.head.next
            self.size -= 1

    def print_list(self):
        p = self.head
        while True:
            if p.next != None:
                print(p.item, '->', end=' ')
            else:
                print(p.item)
                break
            p = p.next

    def SLqueue(self):
        while True:
            num = int(input("Input number: "))
            if num == 0:
                self.delete()
            elif num == -1:
                return
            else:
                self.insert(num)
            if self.is_empty() == False:
                self.print_list()
                print("Head:", self.head.item, "Tail:",  self.tail.item)
# s = SList()
# s.SLqueue()

class PSList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        if self.size == 10:
            print("Queue is overflowed")
        else:
            if self.is_empty():
                self.head = self.Node(item, None)
                self.tail = self.head
            else:
                p = self.Node(item, None)
                self.tail.next = p
                self.tail = p
            self.size += 1

    def delete(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.head = self.head.next
            self.size -= 1

    def print_list(self, node):
        if self.is_empty(): # 큐가 빌경우 함수종료
            return
        if node.next == None:
            print(node.item)
            return
        else:
            print(node.item, '->', end=' ')
            self.print_list(node.next)

    def SLqueue(self):
        while True:
            num = int(input("Input number: "))
            if num == 0:
                self.delete()
            elif num == -1:
                self.print_list(self.head)
                return
            else:
                self.insert(num)
# s = PSList()
# s.SLqueue()
# def push(item):  # 삽입 연산
#     stack.append(item)
#
#
# def peek():  # top 항목 접근
#     if len(stack) != 0:
#         return stack[-1]
#
#
# def pop():  # 삭제 연산
#     if len(stack) != 0:
#         item = stack.pop(-1)
#         return item
#
#
# stack = []
# push('apple')
# push('orange')
# push('cherry')
# print('사과, 오렌지, 체리  push 후:\t', end='')
# print(stack, '\t<- top')
# print('top 항목: ', end='')
# print(peek())
# push('pear')
# print('배 push 후:\t\t', end='')
# print(stack, '\t<- top')
# pop()
# push('grape')
# print('pop(), 포도 push 후:\t', end='')
# print(stack, '\t<- top')
#
# class Node:  # Node 클래스
#     def __init__(self, item, link):  # Node 생성자
#         self.item = item
#         self.next = link
#
#
# def push(item):  # push 연산
#     global top
#     global size
#     top = Node(item, top)
#     size += 1
#
#
# def peek():  # peek 연산
#     if size != 0:
#         return top.item
#
#
# def pop():  # pop 연산
#     global top
#     global size
#     if size != 0:
#         top_item = top.item
#         top = top.next
#         size -= 1
#         return top_item
#
#
# def print_stack():  # 스택 출력
#     print('top ->\t', end='')
#     p = top
#     while p:
#         if p.next != None:
#             print(p.item, '-> ', end='')
#         else:
#             print(p.item, end='')
#         p = p.next
#     print()
#
#
# top = None
# size = 0
# push('apple')
# push('orange')
# push('cherry')
# print('사과, 오렌지, 체리  push 후:\t', end='')
# print_stack()
# print('top 항목: ', end='')
# print(peek())
# push('pear')
# print('배 push 후:\t\t', end='')
# print_stack()
# pop()
# push('grape')
# print('pop(), 포도 push 후:\t', end='')
# print_stack()

class stack:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        self.top = self.Node(item, self.top)
        self.size += 1


    def peek(self):
        if self.size != 0:
            return self.top.item


    def pop(self):
        if self.size != 0:
            top_item = self.top.item
            self.top = self.top.next
            self.size -= 1
            return top_item


    def print_stack(self):
        print('top ->\t', end='')
        p = self.top
        while p:
            if p.next != None:
                print(p.item, '-> ', end='')
            else:
                print(p.item, end='')
            p = p.next
        print()

st = stack()
st.push(1)
st.push(2)
st.push(3)
st.print_stack()
print(st.peek())
st.push(4)
st.print_stack()
st.pop()
print(st.pop())
st.print_stack()
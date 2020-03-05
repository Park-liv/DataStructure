class Node:
    def __init__(self, item, left=None, right=None):
        self.item  = item
        self.left  = left
        self.right = right

class BinaryTree:
    flag = 0
    def __init__(self):
        self.root = None

    def preorder(self, n):
        if n != None:
            print(str(n.item),' ', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        if n != None:
            if n.left:
                print('( ', end='')
                if n.item in operator and n.left.item in operator:
                    if pref(n.item) > pref(n.left.item):
                        BinaryTree.flag += 1
                        print('( ', end='')
                self.inorder(n.left)
            print(str(n.item),'', end='')
            if n.right:
                if n.item in operator and n.right.item in operator:
                    if pref(n.item) > pref(n.right.item):
                        BinaryTree.flag += 1
                        print('( ', end='')
                self.inorder(n.right)
                if BinaryTree.flag > 0:
                    BinaryTree.flag -= 1
                    print(') ', end='')
                print(') ', end='')

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item),' ', end='')

operator = ['*', '/', '+', '-']
bracket = ['(', ')']

def is_number(x):
    if x not in operator and x not in bracket:
        return True
    else:
        return False

def pref(x):
    if x is '*' or x is '/':
        return 1
    elif x is '+' or x is '-':
        return 0

def In2Post(infix):
    stack = []
    postfix = []
    for c in infix:
        if is_number(c):
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while True:
                x = stack.pop()
                if x == '(':
                    break
                postfix.append(x)
        elif c in operator:
            p = pref(c)
            while len(stack) > 0:
                top = stack[-1]
                if top in bracket:
                    break
                if pref(top) <= p:
                    break
                postfix.append(stack.pop())
            stack.append(c)
    while len(stack) > 0:
        postfix.append(stack.pop())
    return postfix

def Post2Tree(pf):
    bt = BinaryTree()
    stack = []
    for i in range(len(pf)):
        if pf[i] in operator:
            bt.root = Node(pf[i])
            bt.root.right = stack.pop(-1)
            bt.root.left = stack.pop(-1)
            stack.append(bt.root)
        else:
            stack.append(Node(pf[i]))
    n = stack.pop()
    print("전위표기: ", end='')
    bt.preorder(n)
    print("\n중위표기: ", end='')
    bt.inorder(n)
    print("\n후위표기: ", end='')
    bt.postorder(n)

# infix = input()
# infix = list(infix)
# infix = [ '2', '*', '(', '5', '+', '7', ')', '+', '8']
infix = [ '2', '+', '3', '*', '4']
pf = In2Post(infix)
# print(pf)
Post2Tree(pf)
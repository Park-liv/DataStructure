class Node:
    def __init__(self, item, left=None, right=None):
        self.item  = item
        self.left  = left
        self.right = right

class BinaryTree:
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
                self.inorder(n.left)
            print(str(n.item),' ', end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item),' ', end='')


bt = BinaryTree()
n1 = Node('-')  #35페이지 트리 이용
n2 = Node('/')
n3 = Node('+')
n4 = Node('*')
n5 = Node('+')
n6 = Node('*')
n7 = Node('6')
n8 = Node('+')
n9 = Node('3')
n10 = Node('-')
n11 = Node('2')
n12 = Node('3')
n13 = Node('-')
n14 = Node('3')
n15 = Node('1')
n16 = Node('9')
n17 = Node('5')
n18 = Node('7')
n19 = Node('4')
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8
n4.right = n9
n5.left = n10
n5.right = n11
n6.left = n12
n6.right = n13
n8.left = n14
n8.right = n15
n10.left = n16
n10.right = n17
n13.left = n18
n13.right = n19
bt.root = n1

print("전위표기: ", end='')
bt.preorder(bt.root)
print("\n중위표기: ", end='')
bt.inorder(bt.root)
print("\n후위표기: ", end='')
bt.postorder(bt.root)
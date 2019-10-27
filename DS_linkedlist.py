from slist import SList

if __name__ == '__main__':
    s = SList()
    # n = s.Node(1, None)
    # m = s.Node(2, n)
    # print(n.item)
    # print(n.next)
    # print(m.item)
    # print(m.next)
    # head = m
    # print(head)
    # print(m)
    # l = s.Node(3, m)
    # print(l.next.next.item)
    # print(n)
    head = s.Node(1,None)
    head = s.Node(2,head)
    head = s.Node(3,head)
    s.print_list(head)
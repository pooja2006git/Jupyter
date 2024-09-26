class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n1 = Node(5)
n2 = Node(10)
n3 = Node(23)
n4 = Node(100)

n1.next = n2
n2.next = n3

currNode = n1
while currNode is not None:
    if currNode.next is not None:
        print(currNode.val, end="->")
    else:
        print(currNode.val)
        if currNode == n3:
            currNode.next = n4
    currNode = currNode.next

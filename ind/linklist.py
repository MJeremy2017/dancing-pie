class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


class LinkedList:
    def __init__(self, head):
        self.head = head

    def find(self, index):
        i = 0
        node = self.head
        while node:
            if i == index:
                return node.val
            node = node.nxt
            i += 1
        if index > i:
            return -1

    def insert(self, index, value):
        prev, curr = None, self.head
        node = Node(value)
        i = 0
        while curr:
            if index == i:
                if i == 0:
                    node.nxt = curr
                    return node
                else:
                    prev.nxt = node
                    node.nxt = curr
                    return self.head
            prev = curr
            curr = curr.nxt
            i += 1
        prev.next = node
        return self.head
            

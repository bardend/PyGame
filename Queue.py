class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def front(self):
        return self.head.data

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else :
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        self.head = self.head.next



q = Queue()
q.push("Ricardo")
q.push("Emanuel")
q.push("Mika")
q.push("RRRAAA")

while q.isEmpty() == False:
    print(q.front())
    q.pop()

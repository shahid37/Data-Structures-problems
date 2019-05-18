class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        new_element = Element(data)
        new_element.next = self.top
        self.top = new_element

    def print(self):
        current = self.top
        if self.top:
            while current.next:
                print("[" + str(current.value) + "]")
                current = current.next
            print("[" + str(current.value) + "]")
        else:
            print("list is empty")

    def pop(self):
        if self.top is not None:
            first_node = self.top
            self.top = self.top.next
            print('deleted node: ' + str(first_node.value))
            del first_node
        else:
            print("list is empty")

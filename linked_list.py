import copy


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def print(self):
        current = self.head
        if self.head:
            while current.next:
                print("[" + str(current.value) + "]", end=' ---> ')
                current = current.next
            print("[" + str(current.value) + "]", end='')
        else:
            print("list is empty")

    def prepend(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def get_length(self):
        length = 0
        current = self.head
        if self.head:
            while current.next:
                length = length + 1
                current = current.next
            length = length + 1
        return length

    def delete_from_end(self):
        last = self.head
        second_last = self.head
        while last.next:
            second_last = last
            last = last.next

        second_last.next = None
        print('deleted node: ' + str(last.value))
        del last

    def delete_from_start(self):
        first_node = self.head
        self.head = self.head.next
        print('deleted node: ' + str(first_node.value))
        del first_node

    # position should be 2 or greater as well as less than the length of the list
    def add_at(self, new_element, position):
        if self.get_length() > position and self.get_length() >= 2:
            current = self.head
            for currentPosition in range(1, position-1):
                current = current.next

            new_element.next = current.next
            current.next = new_element

        else:
            print('Wrong position')

    def delete_from(self, position):
        if self.get_length() > position and self.get_length() >= 2:
            current = self.head
            for currentPosition in range(1, position-1):
                current = current.next

            deleted_node = current.next
            current.next = current.next.next
            print('deleted node: ' + str(deleted_node.value))
            del deleted_node

        else:
            print('Wrong position')

    def merge(self, other_list):
        list1 = copy.deepcopy(self)
        list2 = copy.deepcopy(other_list)
        current = list1.head
        if list1.head:
            while current.next:
                current = current.next

            current.next = list2.head
        return list1

    def slice(self, lower_index, uper_index):
        list_to_be_sliced = copy.deepcopy(self)
        first = list_to_be_sliced.head
        if list_to_be_sliced.head:
            for current in range(1, lower_index):
                first = first.next
        last = list_to_be_sliced.head
        if list_to_be_sliced.head:
            for current in range(1, uper_index):
                last = last.next
        list_to_be_sliced.head = first
        last.next = None
        return list_to_be_sliced

    def splice(self, start, end):
        list_to_be_sliced = copy.deepcopy(self)
        first = list_to_be_sliced.head
        if list_to_be_sliced.head:
            for current in range(1, start):
                first = first.next

        last = list_to_be_sliced.head
        if list_to_be_sliced.head:
            for current in range(1, end):
                last = last.next
        first.next = last.next

        return list_to_be_sliced

    def deep_splice(self, start, delete_count):
        list_to_be_sliced = copy.deepcopy(self)
        first = list_to_be_sliced.head
        if list_to_be_sliced.head:
            for current in range(1, start):
                first = first.next

        last = list_to_be_sliced.head
        if list_to_be_sliced.head:
            for current in range(1, delete_count+start):
                last = last.next
        first.next = last.next

        return list_to_be_sliced

    def is_exists(self, element):
        number = self.head
        while number:
            if element.value == number.value:
                return True
            number = number.next
        return False

    def find(self, index):
        if self.get_length() >= index or self.get_length() >= 1:
            current = self.head
            count = 0

            while current:
                if count == index:
                    return current.value
                count += 1
                current = current.next
        else:
            print("wrong index")

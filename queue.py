class Queue:

    def __init__(self):
        self.queue = list()

    def add_toq(self, data_val):

        # Insert method to add element
        if data_val not in self.queue:
            self.queue.insert(0, data_val)
            return True
        return False

    def size(self):
        return len(self.queue)

    def remove_fromq(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return \
            print("No elements in Queue!")


The_Queue = Queue()
The_Queue.add_toq("Mon")
The_Queue.add_toq("Tue")
The_Queue.add_toq("Wed")
print(The_Queue.size())
print(The_Queue.remove_fromq())
print(The_Queue.remove_fromq())

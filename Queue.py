class queue:
    def __init__(self):
        self.list = []

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        dequeue_elem = self.list.pop(0)
        return dequeue_elem

    def empty(self):
        empty_elem = self.len(list)
        if empty_elem == 0:
            return True
        else:
            return empty_elem




class stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        pop_elem = self.list.pop()
        return pop_elem

    def empty(self):
        empty_elem = self.len(list)
        if empty_elem == 0:
            return True
        else:
            return empty_elem

# оба эти класса должны обладать методами push, pop, empty

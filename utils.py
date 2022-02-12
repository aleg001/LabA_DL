class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __next__(self):
        return next(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __clear__(self):
        self.items = []

    def __push__(self, item):
        self.items.append(item)

    def __pop__(self):
        return self.items.pop()

    def __peek__(self):
        return self.items[-1]

    def __isEmpty__(self):
        return self.items == []

    def __size__(self):
        return len(self.items)

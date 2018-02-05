def create_ascending_list(length):
    assert length > 0
    first = current = create_list(1)
    i = 2
    while i <= length:
        current.next = Node(i)
        current.next.prev = current
        current = current.next
        i += 1
    return first


def create_list(first):
    return Node(first)


class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

    def remove_from_chain(self, first):
        if self.next is not None:
            self.next.prev = self.prev
        if self.prev is None:
            return self.next
        self.prev.next = self.next
        return first

    def add_to_chain(self, new_next):
        if new_next is not None:
            new_next.prev = self
        self.next = new_next
        self.prev = None
        return self


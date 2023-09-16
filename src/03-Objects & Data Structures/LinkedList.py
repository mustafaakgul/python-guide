class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None
class LinkedList:
    def __init__(self):
        self._root = None

    # O(1)
    def insert_first(self, value):
        new_node = ListNode(value)
        new_node._next = self._root
        self._root = new_node

    # O(n)
    def insert_last(self, value):
        new_node = ListNode(value)
        if self._root == None:  # empty list
            self._root = new_node
        else:   # full list
            current_node = self._root
            while current_node != None:
                if current_node._next == None:
                    break
                else:
                    current_node = current_node._next
            current_node._next = new_node

    # O(n)
    def find(self, value):
        current_node = self._root
        while current_node != None:
            if current_node._value == value:
                return True
            else:
                current_node = current_node._next
        return False

    # O(n)
    def size(self):
        count = 0
        current_node = self._root
        while current_node != None:
            count += 1
            current_node = current_node._next
        return count

    # O(1)
    def remove_first(self):
        if self._root != None:
            self._root = self._root._next

    def print(self):
        print("[", end="")

        current_node = self._root
        while current_node != None:
            print(str(current_node._value), end=",")
            current_node = current_node._next
        print("]")

m = LinkedList()

m.insert_first(3)
m.print()

m.insert_first(6)
m.print()

m.insert_last(5)
m.print()
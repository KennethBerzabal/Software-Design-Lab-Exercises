class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

class _Node:
    __slots__ = '_element', '_prev', '_next'

def __init__(self, element, prev, nxt):
    self._element = element
    self._prev = prev
    self._next = nxt

def __init__(self):
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer
    self._trailer._prev = self._header
    self._size = 0

def __len__(self):
    return self._size

def is_empty(self):
    return self._size == 0

def _insert_between(self, e, predecessor, successor):
    newest = self._Node(e, predecessor, successor)
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

def _delete_node(self, node):
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element
    node._prev = node._next = node._element = None
    return element

class PositionalList(_DoublyLinkedBase):

    class Position:
         """An abstraction representing the location of a single element."""

def __init__(self, container, node):
    self._container = container
    self._node = node


def element(self):
    return self._node._element

def __eq__(self, other):
    return type(other) is type(self) and other._Node is self._node

def __ne__(self, other):
    return not (self == other)
class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

class _Node:
    __slots__ = '_element', '_prev', '_next'

def __init__(self, element, prev, nxt):
    self._element = element
    self._prev = prev
    self._next = nxt

def __init__(self):
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer
    self._trailer._prev = self._header
    self._size = 0

def __len__(self):
    return self._size

def is_empty(self):
    return self._size == 0

def _insert_between(self, e, predecessor, successor):
    newest = self._Node(e, predecessor, successor)
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

def _delete_node(self, node):
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element
    node._prev = node._next = node._element = None
    return element

class PositionalList(_DoublyLinkedBase):

    class Position:
         """An abstraction representing the location of a single element."""

def __init__(self, container, node):
    self._container = container
    self._node = node


def element(self):
    return self._node._element

def __eq__(self, other):
    return type(other) is type(self) and other._Node is self._node

def __ne__(self, other):
    return not (self == other)


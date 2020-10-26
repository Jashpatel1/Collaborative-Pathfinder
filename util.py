import pdb

INVALID = -999
HARD_PLACE = -999

ANY_TIME = -999
SOMETIME = 25
tLIMIT = 25

TWAIT = 0
WAIT_FACTOR = 0.51

MAX_STEPS = 45

UNOCCUPIED = 0
IS_ROCK = -99

MOVE_SPEED = 1
MSG_BUFFER_SIZE = 3

FRAME_HEIGHT = 350
FRAME_WIDTH = 600

FRAME_MARGIN = 10
CELL_MARGIN = 5

MAX_AGENTS_IN_CELL = 1


class Actions(object):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3
    WAIT = 4


COLORS = ['white', 'green', 'blue', 'black',
          'red', 'magenta', 'cyan', 'yellow']


def extract_fn(a):
    # print 'a :', a, 'Extract :', a[:-1]
    return a
    # return a[1:]


def euclidean_dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


def manhattan_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def heapsort(l):
    q = PriorityQueue()
    for (i, x) in enumerate(l):
        q.update(i, x)
    return [q.pop_smallest()[1] for x in l]


def _parent(i):
    return (i - 1)


def _lchild(i):
    return 2 * i + 1


def _rchild(i):
    return 2 * i + 2


def _children(i):
    return (_lchild(i), _rchild(i))


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._keyindex = {}
        self.tie_breaker = None

    def __len__(self):
        return len(self._heap)

    def __contains__(self, key):
        return key in self._keyindex

    def _key(self, i):
        """
        Returns the key value of the given node.
        """
        return self._heap[i][0]

    def _priority(self, i):
        """
        Returns the priority of the given node.
        """
        return self._heap[i][1]

    def _swap(self, i, j):
        """
        Swap the positions of two nodes and update the key index.
        """
        (self._heap[i], self._heap[j]) = (self._heap[j], self._heap[i])
        (self._keyindex[self._key(i)], self._keyindex[self._key(j)]) = (
            self._keyindex[self._key(j)], self._keyindex[self._key(i)])

    def _heapify_down(self, i):
        """
        Solves heap violations starting at the given node, moving down the heap.
        """

        children = [c for c in _children(i) if c < len(self._heap)]

        # This is a leaf, so stop
        if not children:
            return

        # Get the minimum child
        min_child = min(children, key=self._priority)

        # If there are two children with the same priority, we need to break the tie
        if self.tie_breaker and len(children) == 2:
            c0 = children[0]
            c1 = children[1]
            if self._priority(c0) == self._priority(c1):
                min_child = c0 if self.tie_breaker(
                    self._key(c0), self._key(c1)) else c1

        # Sort, if necessary
        a = self._priority(i)
        b = self._priority(min_child)
        if a > b or (self.tie_breaker and a == b and not self.tie_breaker(self._key(i), self._key(min_child))):
            # Swap with the minimum child and continue heapifying
            self._swap(i, min_child)
            self._heapify_down(min_child)

    def _heapify_up(self, i):
        """
        Solves heap violations starting at the given node, moving up the heap.
        """
        # This is the top of the heap, so stop.
        if i == 0:
            return

        parent = _parent(i)
        a = self._priority(i)
        b = self._priority(parent)
        if a < b or (self.tie_breaker and a == b and self.tie_breaker(self._key(i), self._key(parent))):
            self._swap(i, parent)
            self._heapify_up(parent)

    def peek_smallest(self):
        """
        Returns a tuple containing the key with the smallest priority and its associated priority.
        """
        return self._heap[0]

    def pop_smallest(self):
        """
        Removes the key with the smallest priority and returns a tuple containing the key and its associated priority
        """

        # Swap the last node to the front
        self._swap(0, len(self._heap) - 1)

        # Remove the smallest from the list
        (key, priority) = self._heap.pop()
        del self._keyindex[key]

        # Fix the heap
        self._heapify_down(0)

        return (key, priority)

    def update(self, key, priority):
        """
        update(key, priority)
        If priority is lower than the associated priority of key, then change it to the new priority. If not, does nothing.

        If key is not in the priority queue, add it.

        Return True if a change was made, else False.
        """

        if key in self._keyindex:
            # Find key index in heap
            i = self._keyindex[key]

            # Make sure this lowers its priority
            if priority > self._priority(i):
                return False

            # Fix the heap
            self._heap[i] = (key, priority)
            self._heapify_up(i)
            return True
        else:
            self._heap.append((key, priority))
            self._keyindex[key] = len(self._heap) - 1
            self._heapify_up(len(self._heap) - 1)
            return True

    def is_empty(self):
        """
        Returns True if the queue is empty empty, else False.
        """
        return len(self) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()

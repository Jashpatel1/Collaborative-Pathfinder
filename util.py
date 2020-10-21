def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heapsort(l):
    q = PriorityQueue()
    for (i, x) in enumerate(l):
        q.update(i, x)
    return [q.pop_smallest()[1] for x in l]

def parent(i):
    return (i - 1) // 2

def lchild(i):
    return 2 * i + 1

def rchild(i):
    return 2 * i + 2

def children(i):
    return (lchild(i), rchild(i))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

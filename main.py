movingObs = [
    {0, 0, 3, 4},
    {1, 2, 0, 5},
    {5, 9, 6, 0},
    {4, 0, 0, 4}
]

def manhattanDistance(self, start, end):
    xs, ys = start
    xd, yd = end 
    return abs(xs - xd) + abs(ys - yd)


class AStar:
    def constraint_object(self, x, y, time):
        for i in movingObs[{x, y}]:
            if i == time:
                return False
        return True
    
    def search(self, start, end):
        x1, y1 = start
        x2, y2 = end
        t = 0
        while constraint_object(x1, y1, t) == False:
            t += 1
        open = set()
        close = set()
        origin = x1, y1, t, t + manhattanDistance(start, end)
        open.add(origin)

        while len(open) > 0:
            temp = -1
            for pos in open:
                if temp == -1:
                    node = pos
                else:
                    x, y, t, f = pos
                    if f < temp:
                        node = pos

            x, y, t, f = node
            if x == x2 & y == y2:
                break

            open.remove(node)
            close.add(node)

            for i in range(9):
                xt = x + i % 3 - 1
                yt = y + i % 3 - 1
                if xt not in range(10) | yt not in range(10) | constraintMap(x, y, xt, yt):
                    continue
                child = x, y, t + 1, -1
                if close.count(child) == 0:
                    

                    

            
import util


def find_path(neighbour_fn,
              start,
              end,
              cost=lambda pos: 1,
              passable=lambda pos, constraints=None: True,
              heuristic=util.manhattan_dist,
              constraints=None):
    """
    Returns the path between two nodes as a list of nodes using the A*
    algorithm.
    If no path could be found, an empty list is returned.
    The cost function is how much it costs to leave the given node. This should
    always be greater than or equal to 1, or shortest path is not guaranteed.
    The passable function returns whether the given node is passable.
    The heuristic function takes two nodes and computes the manhattan distance 
    between the two.
    """
    # tiles to check (tuples of (x, y), cost)
    pq = util.PriorityQueue()
    pq.update(start, 0)

    # tiles we've been to
    visited = set()

    # associated G and H costs for each tile (tuples of G, H)
    costs = {start: (0, heuristic(start, end))}

    # parents for each tile
    parents = {}

    if(heuristic(start, end) == 0):
        return [start]

    while pq and (end not in visited):
        cur, c = pq.pop_smallest()

        visited.add(cur)

        # check neighbours
        for n in neighbour_fn(cur):
            # skip it if we've already checked it, or if it isn't passable
            if ((n in visited) or
                    (not passable(n, constraints))):
                # print 'Nbor: ', n, (not passable(n, constraints)), (util.extract_fn(n) in visited)
                continue

            if not (n in pq):
                # we haven't looked at this tile yet, so calculate its costs
                g = costs[cur][0] + cost(cur)
                h = heuristic(n, end)
                costs[n] = (g, h)
                parents[n] = cur
                pq.update(n, g + h)
            else:
                # if we've found a better path, update it
                g, h = costs[n]
                new_g = costs[cur][0] + cost(cur)
                if new_g < g:
                    g = new_g
                    pq.update(n, g + h)
                    costs[n] = (g, h)
                    parents[n] = cur
            # print '\nVisited: ', visited
            # print '\nParents: ', parents

    # we didn't find a path
    if end not in visited:
        return [], 32767

    # build the path backward
    path = []
    while end != start:
        path.append(end)
        end = parents[end]
    path.append(start)
    path.reverse()

    return path, sum(costs[start])

# keep looping until all paths have been checked

def bfs(graph, start, goal):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until all paths have been checked

    while queue:
        # dequeue the first path from the dequeue
        path = queue.pop(0)
        # get the last node from the paths
        node path[-1]
        # have this node been checked?
        if node not in explored:
            neighbors = graph[node]

        # go through all neighbors nodes and construct a new paths

        for people in neighbors:
            new_path = list(path)
            new_path.append(people)
            # add this new path to our queue
            queue.append(new_path)
            # end condition
            if people == goal:
                return new_path
        explored.append(node)

    return 'No path found'

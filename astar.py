import time,random
start_time = time.time()

def path_finder(matrix):
    # input 2D array full of integers
    # integer element = cost of movement
    length = len(matrix)
    goal = (length-1, length-1)
    # first two coordinate, third one is the cost, last is heuristics
    start = (0,0,0,0)

    # store the cost of a node
    visited = {(0,0):0}
    unexplored = [start]
    parent = {}

    # run until unexplored exists
    while unexplored:
        # sorting by weight, cost/ search the node that is closest to the goal first
        unexplored = sorted(unexplored, key = lambda x:x[3])

        # smallest wegithed vertex from unexplored
        minNode = unexplored.pop(0)

        x,y,current_weight,_ = minNode

        # parent node or child node
        px,py = x,y

        # end condition program
        if (px,py) == goal:
            return visited[goal] + matrix[px][py]

        # neighbors
        neighbors = ((x-1,y), (x+1,y), (x,y-1), (x,y+1))
        # make sure I am in the boundary
        real_neighbors = ((x,y) for (x,y) in neighbors if 0 <=x<length and 0<= y <len(matrix[0]))

        # relaxing the edges/ finding the shortest cost
        for cx,cy in real_neighbors:
            cost = current_weight + matrix[cx][cy]
            #subtract x variables from each other/ subtract y variables from each other/ add them together
            dist = abs(goal[0]-cx) + abs(goal[1]-cy)
            #update the shortest cost
            if (cx,cy) not in parent or cost < visited[(cx,cy)]:
                visited[(cx,cy)] = cost
                parent[(cx,cy)] = (px,py)
                unexplored.append((cx,cy,cost,dist))

import random
arr = [[random.randint(0,100) for x in range(100)] for y in range(100)]
print(path_finder(arr))

print("---%s seconds ---" % (time.time()-start_time))

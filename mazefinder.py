def path_finder(maze):
    start = (0,0)
    end = (len(maze)-1, len(maze)-1)
    frontier = [start]
    length = len(maze)
    explored = []


    while frontier:

        # loop through every node in maze
        # u = (0,0)
        for u in frontier:
            # define x, y
            x,y = u
            # find neighbors
            for x, y in if x,y in (x,y-1), (x,y+1), (x-1,y), (x+1,y):
              if 0 <= x < len(maze) and 0 <= y <len(maze):
                  if maze [x][y] != 'W' and (x,y) not in explored:
                      explored.append ((x,y))
                      frontier.append ((x,y))

                      if (x,y) == end:
                          return True
    return False
                

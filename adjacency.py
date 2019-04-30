import pprint
matrix = [[67, 32, 27, 78, 11], [42, 96, 58, 77, 58], [42, 70, 19, 87, 66],
         [44, 91, 29, 60, 0], [32, 21, 94, 13, 100]]

pprint.pprint(matrix)

def get_n (graph,start):

    row,col = start

# going up
    if row > 0:
        up = (row-1, col)
    else:
        up = -1

# going down
    if row < len(matrix)-1:
        down = (row+1, col)

    else:
        down = -1

# going right

    if col < len(matrix)-1:
        right = (row, col+1)
    else:
        right = -1

# going left

    if col > 0:
        left = (row, col-1)
    else:
        left = -1
    return {up, down, left, right}

print(get_n(matrix,(0,0)))

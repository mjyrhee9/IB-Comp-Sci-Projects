def brute_force(points):
    # Time Cost O(n2) of brute force
    # transform into array
    arr = list(points)
    length = len(arr)
    # best distance
    best = (float('Inf'))
    # closest pair of points
    best_pair = None
    # nested for loop to compare all points to each other
    for i in range(length-1):
        for j in range(i+1, length-1):
            # get elements
            man_distance =(abs(arr[i][0]-arr[j][0])+ abs(arr[i][1]-arr[j][1]))
            # compare to best
            if man_distance < best:
                best = man_distance
                best_pair = ((arr[i][0], arr[i][1]), (arr[j][0], arr[j][1]))

    # return best
    return best_pair, best

def closest_pair_helper(x,y):
    length_x = len(x)

    if length_x <= 3:
        return brute_force(x)

    median = length_x//2

    xl = []
    xr = []
    yl = []
    yr = []

    # fill in xl,xr according to median
    for cord_x in x:
        if cord_x[0] <= median:
            xl.append(cord_x)
        else:
            xr.append(cord_x)

    # fill in yl, yrs
    yl = [x for x in y if x in xl]
    yr = [x for x in y if x in xr]
    print(yl)



def closest_pair(x):
    # Merge Sort O(n lng N)
    sorted_x = list(x)
    sorted_y = list(x)
    sorted_x.sort(key=lambda x: x[0])
    sorted_y.sort(key=lambda x: x[1])
    return closest_pair_helper(sorted_x,sorted_y)


test1 = (
  (2,2), # A
  (2,8), # B
  (5,5), # C
  (6,3), # D
  (6,7), # E
  (7,4), # F
  (7,9)  # G
)

print(closest_pair(test1))

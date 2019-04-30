import random
#init 2D array in IB 2Darray = [][]
counter = 0
arr = []
# fill rows
# IB: loop row from 0 to 10

for row in range(10):
# fill cols
    col = []

# IB: loop col from 0 to 5
    for x in range (5):
        col.append(counter)
    counter = counter + 1
    arr.append(col)
print (arr)

# add to 2D 2Darray
# if row.hasNext()
# then 2D array[row][col] = 2Darray[row][value]

# return 2D array

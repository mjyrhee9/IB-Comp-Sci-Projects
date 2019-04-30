m = [[1,2,3],[4,5,6]]
find = 5

# rows
for o in range(len(m)):
    # o = the first array [1,2,3]

    for i in range(len(m[0])):
        if m[o][i] == find:
            print(m[o][i])
            print ('hurray!')

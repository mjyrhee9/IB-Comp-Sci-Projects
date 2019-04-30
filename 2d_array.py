m = [[1,2,3],[4,5,6]]
# find all odd numbers and put them in a new array
new_arr =[]
# rows

for o in range(len(m)):
    # o = the first array [1,2,3]

    for i in range(len(m[0])):
        if (m[o][i]) %2 == 1:
            new_arr.append(m[o][i])
    print(new_arr)

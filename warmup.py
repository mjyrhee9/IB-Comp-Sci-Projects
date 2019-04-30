# You are given a string of space separated numbers,
# and have to return the highest and lowest number.



def hi_low(str):
    new_arr = []
    num= str.split()
    for x in num:
        new_arr.append(int(x))
    print(new_arr)

    highest = 0
    for x in new_arr:
        if x > highest:
                highest = x
    print(highest)


hi_low('100, 20, 200, 4')

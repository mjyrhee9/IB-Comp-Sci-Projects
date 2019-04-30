n = 28
count = 0
while n > 0:
    if n >= 10:
        n = n -10
        count = count + 1

    elif n >= 5:
        n = n - 5
        count = count + 1

    elif n >= 1:
        n = n - 1
        count = count + 1

print (count)

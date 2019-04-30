#Array
#POS = 0
#loop POS from 0 to 19
  #output STUDENTS[POS]
#end loop

#Collection
#loop while Students.hasNext()
  #output STUDENTS.getNext()
#end loop

arr= [12,124,65,32,24,12,7546,45,23]
#index range = 0-8 because len = 9
print(len(arr))

#create a variable to hold index value
pos = 0
for int in arr:
    print(arr[pos])
    pos = pos +1


collection = arr

#collection
while len(collection) > 0:
    print (collection.pop())

# Array of ints that is len 10
# you want to add up and sum all non zero values

POS = 0
COUNT = 0
SUM = 0

loop POS from 0 to 9
    if ARRAY[POS] != 0:
        sum = sum +ARRAY[POS]
        count = count + 1
    end if
end loop

if COUNT > 0:
    output(sum/count)
else:
    output("No non-zero numbers")
end if

# collection
COUNT = 0
SUM=0
loop while COLLECTION.hasNext()
    num = COLLECTION.getNext()
    if num != 0
        COUNT = COUNT + 1
        SUM = NUM + SUM
    end if
end loop

if COUNT > 0:
    output (SUM/COUNT)
else:
    output("no nonzero ints")
end if

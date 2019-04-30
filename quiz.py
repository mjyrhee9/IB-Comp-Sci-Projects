#1.) Given an array of names, write an algorithm to search for a name.
      #Return the index value if found.
arr = ["mom","dad","sister","brother"]

answer = 'False'
for a in range(len(answer)):
    if answer[a] == 'sister'
        answer = "True"
    end if
end loop
output(answer)

# Great job!!!

#2.) Given a collection of ints, write an algorithm to find
      #the average of all even nums

collection = [1,2,3,4,5,6,7,8,9,10]
div = 0
sum = 0

  while collection.hasNext ()
    num = collection.getNext ()
      if num % 2 == 0
        div = div + 1
        sum = sum + num
      end if
  end loop

output(sum/div)

# Perfect!!!

#3.) Given a stack of names, write an algorithm that will return
    # all names that start with a vowel

stack = []
names = []

loop while not stack.isEmpty():
     # no need for count
    letter = stack.pop() # stack.pop()

    if letter[0]== 'a'
        letter[0] = names.push
    elif letter [0] == 'e'
        letter[0] = names.push
    elif letter [0] == 'i'
        letter[0] = names.push
    elif letter [0] == 'o'
        letter[0] = names.push
    elif letter [0] == 'u'
        letter[0] = names.push
    end if
end loop

print (names)




#4.) Given a queue, write an algorithm that will return all names
    #that do not start with a vowel

queue = []
names = []


loop while not queue.isEmpty():
    x = queue.dequeue()
 # no need for count

    if x =! 'a'
        x[count] = names.enqueue
    elif x[count] =! 'e'
        x[count] = names.enqueue
    elif x[count] =! 'i'
        x[count] = names.enqueue
    elif x[count] =! 'o'
        x[count] = names.enqueue
    elif x[count] =! 'u'
        x[count] = names.enqueue
    end if
end loop

print (names)


#5.) Given a 2D array of ints. Write an algorithm that will
    # average all non zero ints.

m = [[1,2,3,0],[4,5,0,6]]
# find all odd numbers and put them in a new array
new_arr =[]
div = 0
sum = 0

# rows

for a in range(len(m)):
    # o = the first array [1,2,3]

    for i in range(len(m[a])):
        if (m[a][i]) =! 0:
            new_arr.push(m(a)[i])
        end if
    end loop
end loop

for pos in range(new_arr)
  num = new_arr[pos]
    sum = sum + num
    div = div + 1
  end if
end loop

output (sum/div)
# Great job!

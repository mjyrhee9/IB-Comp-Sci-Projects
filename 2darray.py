nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#sum and average all even numbers
#num %2 == 0 for even
#init a new collection to hold all even numbers

even_nums = []
# cycle through rows
for rows in nums:
    # cycle through cols
    for cols in rows:
        if cols % 2 ==0:
            even_nums.append(cols)
        #end if
    #end loop
#end loop

#sum and average even numbers
counter = 0
sum
for x in even_nums:
    #add x to x
    sum = x + sum
    # counter increase
    counter = counter +1
#end loop
print (sum//counter)

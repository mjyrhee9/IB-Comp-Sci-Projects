# You have two lists which you will use to create a third
# You will compare list1[x] to list2[y] and populate the third
# List with which every iterators word length is even
# if both are even, then you would add just one case of the word
# you can only use while loops

arr1 = ['woof','mew','bork','craww','tricky']
arr2 = ['borf','meow','growll','chirps','tricky']
new_arr=[]

#outter count
i=0
#inner count
j=0

#outter loop
while i < len(arr1):
    # if index value is even and index value is not in my new array
    if len(arr1[i]) % 2 == 0 and arr1[i] not in new_arr:
        # add it to new array
        new_arr.append(arr1[i])

    # counting
    i = i + 1
    # inner loop
    while j < len (arr2):
        if len(arr2[j]) % 2 ==0 and arr2[j] not in new_arr:
            new_arr.append(arr2[j])
        j = j + 1


print(new_arr)

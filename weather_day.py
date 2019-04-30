# create a 2D array that contains days and a list of their
# highest, lowest, and mean temp
# then
# cycle through this 2d array to
# find the highest of all temps and return that day

# data type: Days => 0-6, temps => 0-2
# row = day
# col = temp
# weather= [[64,75,81], [72,76,80], [90,87,67]]
# highest_temp = 0
# if weather[i][o] > highest_temp
# highest_temp = weather[i][o]

weather = [[64,75,81], [72,76,80], [90,87,67], [77,67,89], [65,54,87], [80,88,76], [78,76,65]]

highest_temp = 0
for o in range(len(weather)):
    for i in range(len(weather[o])):

        if weather[o][i] > highest_temp:
            highest_temp = weather[o][i]

print(highest_temp)

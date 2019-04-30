#output all non zero nums
#output all non zero nums count inclusive
#output all col values of non zero nums for a row

count = 0
for row in range(len(matrix)):

    for col in range(len(matrix)):
        if MAT[row][col] != 0:
            array1.append(MAT[row][col])
            array3.append(col)
            count= count + 1

    array2.append(count)

print(array1)
print(array2)
print(array3)

#pseudocode

count = 0
K = 0
loop for I from 0 to 5
loop for J from 0 to 5
if MAT[I][J]! = 0 then
VALUES[K] = MAT[I][J]
COL[K] = J
K = K + 1
COUNT = COUNT + 1
end if
end loop
ROWC[I] = COUNT
end loop

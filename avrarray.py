array = [1,2,3,4,5,6,7,8,9,10]


for pos in range(9)
  num = array[pos]
  if num % 2 ==0
    sum = sum + num
    div = div + 1
  end if
end loop

output (sum/div)

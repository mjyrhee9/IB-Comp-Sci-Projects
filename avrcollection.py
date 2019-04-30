# find the avr of a collection
# only sum numbers % 3 == 0

# collection

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

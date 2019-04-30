def find_me (arr)
  inner = 0
  while inner < arr.length
    outter = 0
    while outter <= arr.length
      if outter == arr.length
          return arr[inner]
      elsif inner == outter || -(arr[inner]) != arr[outter]
        outter = outter +1
      else
        break
      end
      
      inner = inner+1
    end
  end
  puts "#{outter}, #{inner}"
end

arr1 = [1,-1,2,-2,3]
find_me (arr1)
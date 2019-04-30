def sum_arr (arr)
	if arr.count < 2
		return 0
		puts "This array was empty"
	else
		new_value = arr[-1] + arr[-2] 
		arr.pop (2)
		arr.push(new_value)
		sum_arr (arr)
	end
end

array = [-7,1,14,100,-97]
sum_arr(array)
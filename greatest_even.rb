a = [24, 5, 12, -4, 0, 2, 19]

MaxNumber = 0
for x in a do
	for y in a do
		if y <= x && x>= MaxNumber
			if x.even?
				MaxNumber = x
	
			end
		end
	end

end
puts MaxNumber

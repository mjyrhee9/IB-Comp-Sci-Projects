random_array = [0.5, -7, 10, 3]

def compare(collection)
for number in collection do 
	max_count= 0
	min_count = 0

	for number_comparison in collection do
		if number > number_comparison
			min_count = number_comparison
		end
		if number < number_comparison
			max_count = number_comparison
		end
	end
	
end

puts max_count - min_count

end

# call method

compare(random_array)
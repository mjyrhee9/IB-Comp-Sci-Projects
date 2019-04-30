def digit_sum(n)
	#n.to_s.chars.map(&:to_i)
	n.to_s.chars.inject { |sum,n| sum = sum.to_i + n.to_i}
end

puts digit_sum(12345) 

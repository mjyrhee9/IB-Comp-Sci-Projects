def CountDown(num)
	return num if num <= 0
	puts num
	CountDown(num-1)
end

CountDown(10)
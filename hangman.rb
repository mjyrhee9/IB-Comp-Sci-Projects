@guess_right_array = []
@guess_wrong_array = []
@correct_word_array = ["d","o","g"]  
@correct_word = "dog"
@count = 0

def intro
	puts "Welcome to the game!"
end

def guess
	#Ask to guess
	#Save letter to a variable
	puts "Guess!"
	@guess = gets.chomp
end 

def check
	# if and else/ if it's right then put it in the guess.right_arrary
	# compare input to the answer
	if (@correct_word_array - @guess_right_array).empty? == true
		puts "You win!"
			
	elsif @correct_word.include? @guess
			@guess_right_array.push @guess
			puts "Good!"
			puts "Right Letter: #{@guess_right_array} // Wrong Letter: #{@guess_wrong_array}"

		
	else @guess_wrong_array.push (@guess)
			puts "Try again!"
			puts "Right Letter: #{@guess_right_array} // Wrong Letter: #{@guess_wrong_array}"

	end
end

def ask_to_play_again
	puts "would you like to play again? (y/n)\n"
	response = gets.chomp
	return response[0] == 'y' || response[0] == 'Y'
end

def play_game
	while @count <= 6
		guess
		check
		@count += 1
	end
end
	







@age_array = []

def intro
	puts "Welcome to the age game!"
end

def ask_name
	puts "What is your name?"
	name = gets.chomp
	puts "Welcome #{name}"
	
end

def ask_age
	puts "How old are you?"
	@age = gets.chomp.to_i
	#Push @age to an array
	@age_array.push(@age)
	#Test @age_array scope
	puts "It worked! #{@age_array}"

	
end

def age_res
	# compare age and an if/else
	if @age <= 13
		puts "OMG #{@age}? you're so young!"
	elsif @age <= 18
		puts "OMG #{@age}? CUTE!"
	elsif @age <= 25
		puts "OMG #{@age}? Such an adult!"
	else @age > 25
		puts "OMG #{@age}? Someone's aging!"
	end

end

def playGame
	askQuestion
	checkAge
end

def ask_to_play_again
	puts "would you like to play again? (y/n)\n"
	response = gets.chomp
	return response[0] == 'y' || response[0] == 'Y'
end
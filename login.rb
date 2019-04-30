
def intro 
	puts "Hi"
end 

def username
	puts "Make a new username"
	@your_username = gets.chomp
end

def password
	puts "Make a new password"
	@your_password = gets.chomp
end

def check_username
	puts "What is your username?"
	@username = gets.chomp
	if @your_username == @username
		puts "Yes"
	else 
		puts "Try again"
	end

end

def check_password
	puts "What is your password?"
	@password = gets.chomp
	if @your_password == @password
		puts "You are logged in"
	else
		puts "Try again"
	end

end


def ask_to_play_again
	puts "would you like to play again? (y/n)\n"
	response = gets.chomp
	return response[0] == 'y' || response[0] == 'Y'
end



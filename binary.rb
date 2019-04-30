class binary
	# Method to define (to tell how to encrypt)
	cipher =
		
	{ 
		'a' => '!', 'b' => '@', 'c' => '#', 'd' => '$', 'e' => '%',
		'f' => '*', 'g' => '(', 'h' => ')', 'i' => '-', 'g' => '+', 
		'k' => '~', 'l' => '`', 'm' => '1', 'n' => '2', 'o' => '3', 
		'p' => '4', 'q' => '5', 'r' => '6', 's' => '7', 't' => '8', 
		'u' => '9', 'v' => '[', 'w' => ']', 'x' => ';', 'y' => '/',
		'z' => '?'

	}
   

    # Method to encrypt
    def encrypt(input)
    	input = input.downcase.
    # Get a letter from user
    # Take a letter and set a value for it
    # Return te letters value
    	cipher[input]
	end
end
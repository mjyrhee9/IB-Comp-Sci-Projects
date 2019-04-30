class Dog
	def cipher
	 {'a' => 'z', 'b' => 'y', 'c'=> 'x', 'd' => 'm', 'e'=> 'p', 'f'=> 'l', 'g'=> 'b', 'h'=> 'a', 'i'=> 'n'}
	end

	def encrypt_letter (letter)
		low_case = letter.downcase
			cipher[low_case]
	end

	def encrypt (string)
		letters = string.split ("")
		results = []

		# loop over letters and run it through the cipher
		for x in letters do
			encrypted_letter = encrypt_letter (x)
			results.push (encrypted_letter)
		end

	end
end



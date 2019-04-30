

def cap (word)
	#take out the first letter and capitalize it
	first_letter = word[0].upcase
	#joining the letter that is not upercase to the new upercased letter
	letter_join = first_letter << word
	letter_join.slice!(1)
	#removing the second letter of the joined word
	
	puts letter_join
end

meow = 'woof'
cap(meow)

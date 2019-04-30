require "./agegame.rb"

bask_to_play_again = true

while bask_to_play_again == true

	intro
	ask_name
	ask_age
	age_res
	bask_to_play_again = ask_to_play_again

end
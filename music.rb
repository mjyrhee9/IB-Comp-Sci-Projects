@songs = []
@artists = []

def intro 
	puts "Ready for some music? Choose songs or artists!"
end 


def song_or_artist
	puts "Would you like to work with song or artist?:s/a"
	song_or_artist_user = gets.chomp

	if song_or_artist_user =='s'
		song_add_del
	else
		artist_add_del
	end

end

def song_add_del
	puts "Would you like to add or delete songs?: a/d"
	user_add_delete_decision_s = gets.chomp
	if user_add_delete_decision_s == 'a'
		puts "Which song do you want to add?"
		song_add = gets.chomp
		@song.push(song_add)

	else
		puts "Which song do you want to delete?"
		song_del = gets.chomp
		@song.delete(song_del)
	end
end

def artist_add_del
	puts "Would you like to add or delete artists?: a/d"
	user_add_delete_decision_a = gets.chomp

	if user_add_delete_decision_a == 'a'
		puts "Which artist do you want to add?"
		artist_add = gets.chomp
		@artist.push(artist_add)

	else
		puts "Which artist do you want to delete?"
		artist_del = gets.chomp
		@artist.delete(artist_del)
	end

def showlist
	"@songs" 
	"@artists"
end 

end




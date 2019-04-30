require "./login.rb"

bask_to_play_again = true

while bask_to_play_again ==true
intro
username
password
check_username
check_password
bask_to_play_again = ask_to_play_again
end
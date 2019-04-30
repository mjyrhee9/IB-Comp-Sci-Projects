
# separate each word in the sentence
words = str("Pig latin is fun").split()
# looping through words and print each word with second to last letter with "ay" and first
# letter for every single word in the sentence
    loop for word in words:
        final = (word[1:] + word[0] + "ay", end = " ")
    end loop

output (final)

def pig_it():

    words = str("Pig latin is fun").split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print()

pig_it()

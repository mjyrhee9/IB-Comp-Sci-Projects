#implement the function unique_in_order which takes as argument a sequence and
#returns a list of items without any elements with the same value next to each other
#and preserving the original order of elements

# unique_in_order('AAABBBBCCDDD')== ['A','B','C','D']

# LETTERS = []
# STR = "AAABBBBCCDDD" <= break into an array
# loop while STR.hasNext()
  # if x != LETTERS [-1]
    # LETTERS.addItem(x)

def unique_in_order(str):
    letters = []


    for x in str:
        if len(letters) == 0 or x != letters[-1]:
            letters.append(x)
    print(letters)
    return(letters)

str = "AAABBBBCCDDD"
unique_in_order(str)

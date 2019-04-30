

#ohms_color = []

#ohms_str = input

# while ohms_str.hasNext()
# ohms_color(ohms_str.getNext())

#copying into array
#for x in ohms_str:
  #ohms_color.append(x)

def ohms(str):
    colors = {
           "0": 'black',
           "1": 'brown',
           "2": 'red',
           "3": 'orange',
           "4": 'yellow',
           "5": 'green',
           "6": 'blue',
           "7": 'violet',
           "8": 'gray',
           "9": 'white'
       }
    #ohms_color = []

    #for x in str:
        #ohms_color.append(x)
firstcolor = colors[str[0]]
secondcolor = colors[str[5]]
thirdcolor = colors[str[9]]

    # getting the value from key
    #first_color= colors[ohms]
    #print(ohms_color)

ohms("5")

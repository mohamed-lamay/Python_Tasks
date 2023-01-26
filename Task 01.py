def mutate_string(string, position, character):
    # convirt string to list
    l = list(string)
    #replace characters in refered position
    l[position] = character
    #join characters from list to get string
    string = ''.join(l)

    print (string)

x = input("please enter a string \n")
y = int(input("please enter the position of the char to replace \n"))
z = input("please enter the character \n")
mutate_string(x,y,z)
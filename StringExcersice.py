def char():
    x = "ameen"
    
    for i in x:
        print(i + "\n")
    
    print ("Length if the string is " + str(len(x)))    
    input_char = input("Enter a char : ")
    print (input_char in x)
    
    if input_char in x:
        print ( input_char +" is present in x")
    else:
        print (input_char + " is missing in the x")

def string(slice):
    input_int = int(input ("Enter a number : "))
    if input_int:
        return (slice [:input_int].upper())
    else:
        print ("Try next time")


char()
print (string("Its good to have python knowledge"))


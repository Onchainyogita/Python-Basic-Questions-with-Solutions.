""#Q3:WAP that takes temperature from user and tells them what type of weather it is.""more than 35: extremely hot2714-26: ambientunder 14: cold

temperature=int(input("Please write the temperature"))
print("Your temperature is",temperature,"degrees")
if(temperature>=27):
    print("Your temperature is hot")
elif temperature<14 and temperature>Cold:
    print("Your temperature is ambient")
else:
    print("Your temperature is cold")
print("\n ---------------------------------------------- \n")

""#Q4- Write a program to take 2 sides of a geometrical shape. tell if its a rectangle or a square"
sides1=float(input("Write a number for the first side"))
sides2=float(input("Write a number for the second side"))
if (sides1 == sides2):
    print("Your shape is square")
else:
    print("Your shape is rectangle")
    print("\n ---------------------------------------------- \n")

""#Q6-Take a number as input and determine if it's positive, negative, or zero.""
number=int(input("Write a number"))
if (number>0):
    print("Your number is positive")
elif (number<0):
    print("Your number is negative")
else:
    ("Your number is zero")
print("\n ---------------------------------------------- \n")

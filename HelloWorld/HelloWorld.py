#this is a comment
#and I can add a lot of cool stuff
print ("The monkey eats nuts\n and drinks water from the river")
print(3+6)
print(6*9)
#try using \n! Nifty, an't it?
print("I like oranges\ and bananas to")
#to print the backslash when the next word starts with a n
print("what i I wanted is \\news")
name = input("What is your name?") #lot like Scanner in Java!!
country = input("What country do you live in?")
country = country.upper()
print ("Hello" + name)
print(country)
message = "hello world"
print(message.find("world"))
print(message.count("o"))
print(message.capitalize())
print(message.replace("hello","hi"))
area = 0
height = 10
width = 10
area = height*width/2
print("The area of the plane is %0d "  % area, 42, 50) # This is nifty: one times %0d and then the two numbers
print("My favaroute number is %6d!"% 42) # first 6 spaces then the number
print("The area of the triangle would be {0:f} ".format(area)) # using format is the way to go
print("The area of the" + \
    " box would be {0:d} {1:4d} ".format(42,33)) # the 4 infront of d creates spaces. Using \ to devide sentence?
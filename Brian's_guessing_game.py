#This is a guessing game
import random
#lets input a random module
invisible = random.randrange(1, 201)
print(invisible)

estimate  = int(input("Hi there! please input an integer : "))

#lets add some if else statements
if estimate  == invisible:
	print("You got it :)!")
elif estimate  < invisible:
	print("Try a higher number, please run the program again.")
else:
	print("Try a lower number, please run the program again.")
#The End
'''
I hope you had fun, playing thia simple game it took me a few minutes to make
'''

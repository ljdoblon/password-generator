#Project 1: Password Generator
#Author: Louis John Doblon
#5/30/2020
#Uses 'random' module to create a pseudo-random generated
# from the 'string' module's constants (ascii_letters,
# punctuation and digits. Number of characters for
# each type [numbers, letters, and symbols] are also
# user defined.). os is used to locate the generated
# password text file.
import random
import string
import os

#Generate Password with random and string modules
def generate_password():
	password = []
	for i in range(int(chars)):
		letters = random.choice(string.ascii_letters)
		symbols = random.choice(string.punctuation)
		numbers = random.choice(string.digits)
		password.append(letters)
		password.append(symbols)
		password.append(numbers)

#''.join(*list) to join password list together as a whole string
	final_pass = ''.join(password)
	print("Password Generation Complete! ")
	print(final_pass)

#save the generated password in a .txt file
	generated_password = open("generated_password.txt","w")
	generated_password.write(str(final_pass))
	generated_password.close()

#file locator
def locator():
	print("Generated password saved in: " + os.path.abspath('generated_password.txt'))


print("# PASSWORD GENERATOR #")
startup = input("Generate Password?: ")
try:
	chars = input("How many characters each?: ")
	if (startup == "y" or "Y" or "yes" or "Yes" or "YES"):
		generate_password()
		locator()
except ValueError:
	print("Invalid Input")



#this project is subject to improvements and revisions
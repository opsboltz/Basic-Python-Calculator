#Getting Input from user
first = floar(input("Welcome to the Calculator, What is your first number: "))
second = float(input("Whatis your second number: "))
sign = input("What sign do you want to use (e.g., -,/,+,*,^): ")

if sign == '+':
	answer = first + second
elif sign == '-':
	answer = first - second
elif sign == '*':
	answer = first * second
elif sign = '/':
	answer = first / second
else
	awnser = "invalid sign"

##printing the answer
print ("THe answer is: ", answer)

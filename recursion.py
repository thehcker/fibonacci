# Prompt the user to enter a number
n = int(input("Enter the number of Fibonacci sequence you would like to display? "))
count = 0
number1 = 0
number2 = 1
def fibonacci(nterms):
	global count,number1,number2
	# check if the number of terms is valid
	if nterms <= 0:
	   print("Please enter a positive integer")
	elif nterms == 1:
	   print(number2)
	else:
	   print("Fibonacci sequence upto",nterms,"terms:")
	   
	   while count < nterms:
	       print(number1,end=' , ')
	       term = number1 + number2
	       # update values
	       number1 = number2
	       number2 = term
	       count += 1
fibonacci(n)

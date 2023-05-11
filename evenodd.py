def odd_or_even(number):
	if(number % 2 == 0):
		print(number, " is even")
	else:
		print(number, " is odd")

num = int(input("Enter number:"))
odd_or_even(num)
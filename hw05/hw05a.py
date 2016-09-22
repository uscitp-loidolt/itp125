user_sum = raw_input("Enter a number a number 1 - 1000: ")
y = int (user_sum)
sum = 0

for n in range(0,y):

	if n % 3 == 0:
		sum = n + sum

	elif n % 5 == 0:
		sum += n

print "The sum of the multiples 3 & 5 below your number is", sum 

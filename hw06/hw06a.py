x = 600851475143
a = 2
while (x > a):
	if (x % a == 0):
		x = x/a
		a = 2
	else:
		a+=1;
print("Largest Prime Factor: %d" % (a));

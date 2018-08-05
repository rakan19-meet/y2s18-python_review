# Write your solution for 1.4 here!

def is_prime(x):
	for i in range (2,x,1):
		if x % i ==0:
			return "x isnt a prime num"
	return "x is a prime num"
print(is_prime(5191))


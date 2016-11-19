


#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

from euler_functions import isPrime

def main():

	index = 1
	i = 3
	while(True):
		if(isPrime(i)):
			index+=1
			if(index==10001):
				print(i)
				return True
		i+=2




main()
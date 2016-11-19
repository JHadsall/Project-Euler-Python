

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

from euler_functions import isPrime
import math

def main():
	for i in range(int(math.sqrt(600851475143)),2,-1):
		if(600851475143%i==0):
			if(isPrime(i)):
				print(i)
				return i


main()
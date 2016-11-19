

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

from euler_functions import isPalindrome
def main():
	largest = 0
	for i in range(999,100,-1):
		for j in range(999,100,-1):
			product = i*j
			if(isPalindrome(product)):
				if(product>largest):
					largest = product

	print(largest)


main()
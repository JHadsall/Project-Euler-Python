def isEven(number):
	return number%2 == 0


import math
def isPrime(number):
	if(number == 1):
		return False
	else:
		for i in range(2,int(math.sqrt(number))+1):
			if(number%i==0):
				return False;
		return True
		
	return False


def isPalindrome(number):
	digitsLength = len(str(number))-1
	half = digitsLength/2
	if(not isEven(digitsLength)):
		half = (digitsLength/2)+1
	for i in range(0,half):
		if(str(number)[i] == str(number)[digitsLength-i]):
			continue
		else:
			return False
	return True


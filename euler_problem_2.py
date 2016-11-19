


#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.#

from euler_functions import isEven

def main():
	sum = 2
	fibOne = 1
	fibTwo = 2
	while(fibTwo<4000000):
		newFib = fibOne + fibTwo
		fibOne = fibTwo
		fibTwo = newFib
		
		if(isEven(newFib)):
			sum+=newFib

	print(sum)




main()
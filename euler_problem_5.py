
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



def main():
	index = 2520
	while(True):
		for i in range(20,10,-1):
			if(not index%i == 0):
				break
			elif(i == 11):
				print(index)
				return True

		index+=2520
		
main()

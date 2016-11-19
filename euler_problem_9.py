
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math
def main():
	for i in range(1,334):
		for j in range(i+1,1000):
			a = i**2
			b = j**2
			cSqrd = a+b
			c = math.sqrt(cSqrd)
			sum = int(i+j+c)
			if(sum>1000):
				break
			if((c-int(c))==0):
				if(sum==1000):
					print(str(i) + ' ' + str(j) +' '+ str(c) +'  '+ str(sum))
					print(int(i*j*c))
				

		
	





main()
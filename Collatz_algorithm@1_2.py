'''
Created on Nov 12, 2018
Collatz algorithm:
Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1
@author: Lavikas
'''
'''create a function as same process need to be processed and loop the same function (self loop)'''
def collatz_algo(input_num,count=0):
    if input_num == 1:
        return count
    elif input_num %2 ==0:
        return collatz_algo(input_num/2,count+1)
    else:
        return collatz_algo((3*input_num)+1,count+1)

print(collatz_algo(27105615165))
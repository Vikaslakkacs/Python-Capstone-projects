'''
Created on Nov 12, 2018
Collatz algorithm:
Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1
@author: Lavikas
'''
'''Loop the class method until it is one'''
class collatz_algo():    
    
    def algo_validate(self,input_num):
        '''If num is even then divide by 2 else 3n+1'''
        if input_num %2 == 0:
            output_num = input_num /2
        else:
            output_num = ((3*input_num)+1)
        return int(output_num)

'''Ask for input'''
input_num=input('Please enter the number:-')
while True:
    
    if input_num.isnumeric():
        break
    else:
        print('Entered input has other than digits')
        input_num=input('Please re-enter the number:-')

'''Variable to count the number of iterations required to equalize one'''
reccurence_count=0
collatz=collatz_algo()
collatz_num=int(input_num)
while True:
    reccurence_count+=1
    collatz_num=collatz.algo_validate(collatz_num)
    #print(collatz_num)
    if collatz_num == 1:
        break

print(reccurence_count)
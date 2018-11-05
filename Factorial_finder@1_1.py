'''
Created on Nov 5, 2018
To find the factorial of a number given
@author: Lavikas
'''
from warnings import catch_warnings
'''Request for the value'''
num=input('Please provide a number')
while True:
    if num.isnumeric()== True:
        break
    else:
        print('Entered  number has digits other than numeric \n')
        num= input('Re-Enter the number:')
num=int(num)
for facto in range(1,num):
    print(facto)
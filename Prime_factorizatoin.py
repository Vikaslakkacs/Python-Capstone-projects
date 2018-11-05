'''
Created on Oct 16, 2018
find the prime factors of the given number
@author: Lavikas
'''

'''
Process:
-->Find the factors of the Number
--> Take the second number in the list and store it in the result
--> find the factors of the last number in the list and continue till the factor of the number is itself'''

import datetime
'''find the number where the reminder is not zero'''
'''def factors(number):
    factor_list=[]
    for factor in range(1,number+1):
        if number % factor == 0:
            factor_list.append(factor)
    return factor_list
#print(factors(499))'''

''' instead of using the above function you can use lamba function as it is a single statement function'''
factor=lambda number:[factor for factor in range(1,number+1) if number % factor ==0]
'''Now run the process by initializing the list'''
result=[]
number=int(input('Enter the number which you want to get the prime factors'))
#print(datetime.datetime.now())
while True:
    factor_rslt=factor(number)
    result.append(factor_rslt[1])
    if len(factor_rslt) > 2:
        number=factor_rslt[-2]
        continue
    else:
        break
'''printing the result'''
res_string=''
for digit in result:
    res_string +=str(digit) +'*'
print('>>>'+res_string.rstrip('*'))
#print(datetime.datetime.now())

#print(datetime.datetime.now())





''' We found another alternate soution:
--> As we are considering the 2nd and 2nd last element in the list then why calculating all the numbers and storing in the list
-->consider the second element and last second element and apply the same
Eg: factors of 98 are 1,2,7,14,49,98
We are anyways considering the first and second largest factor, where we are inserting 2 into result list
 and again we are finding the factor of 49 which is the second largest and by ignoring the middle ones anyways those are not usefull'''
def first_factor(number):
    for factor in range(2,number+1):
        if number % factor ==0:
            first_factor=factor#Considering the first factor and returning to the result
            return first_factor
            break

def last_factor(number):
    counter=0
    for factor in range (number,1,-1):
        if number % factor ==0:
            counter +=1
            last_factor=factor
            if counter==2:#Considering the second largest factor for the given number
                return last_factor
                break
    return last_factor#if no number is the second largest factor then consider the actual number as the factor and return

number=int(input('Enter the number which you want to get the prime factors'))
#print(datetime.datetime.now())
result=[]
change_num=number#Assign the input to the buffer value which will change according to the function call
'''there are situation where you will come across squares where it will be true as both the values are same
So in order to seggregate it, we are using the 'buffer_num' variable'''
while True:
    buffer_num=change_num
    first_fact=first_factor(change_num)
    result.append(first_fact)#first factor anyways is appended to the result
    last_fact=last_factor(change_num)##check if it has largest factor
    change_num=last_fact#Assign the largest factor to the buffer value
    #print(first_fact)
    #print(last_fact)
    if first_fact== change_num:#check if the first factor is same as the buffer value after considering the larges factor i.,e first factor=last factor
        if change_num != buffer_num:#If yes check if the buffer value is not the input number h
            result.append(first_fact)#Then insert into the list exit
        break

        
'''printing the result'''
#print(result)
res_string=''
for digit in result:
    res_string +=str(digit) +'*'
print('>>>'+res_string.rstrip('*'))      
#print(datetime.datetime.now())


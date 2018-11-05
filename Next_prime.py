'''
Created on Oct 20, 2018
Find the next prime o the selected number
@author: LAVIKAS
'''
'''
we have to find the prime number next to the selected number'''
def digits(number):
    result=[]
    for num in range(2,number+1):
        if number % num ==0:
            result.append(num)
    return result


'''We can find the prime by looping'''
def prime(number):
    prime_num=number
    while True:
        prime_num +=1
        prime_result=digits(prime_num)
        if len(prime_result) == 1:
            print(prime_result[0])
            break;

prime(2159892)
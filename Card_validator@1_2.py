'''
Created on Oct 30, 2018
Program is to validate the credit/debit card
@author: Lavikas
'''
card_num= input('Enter the card details:')
while True:
    if card_num.isnumeric():
        break
    else:
        print('Entered Card number has digits other than numeric \n')
        card_num= input('Re-Enter the card details:')
        
'''Applying the nested for loop which is below mentioned into single statement
card_odd=[i for i in card_num[::2]]
print(card_odd)
card_odd_double=[int(odd_double)*2 for odd_double in [odd_num for odd_num in card_num[::2]]]
'''
'''Picking up the odd and multiplying with two in a single step'''
card_odd_double=[int(odd_num)*2 for odd_num in card_num[::2]]
'''Adding the card digit if the length is two''' 
card_add_odd=[]
for even_digit in card_odd_double:
            str_even=str(even_digit)
            if len(str_even) > 1:
                '''Add the strings and convert it into digitss'''
                #print(str_even)
                even_digit=0
                for single_digit in str_even:
                    even_digit += int(single_digit)
                    if even_digit==10:
                        even_digit = 1
            else:
                even_digit = int(even_digit)
            card_add_odd.append(even_digit)
'''Now add the odd digits and even digits and validate the sum'''

if sum(card_add_odd + [int(even_num) for even_num in card_num[1::2]]) % 10 ==0:
    print('your card is valid')
else:
    print('your card is invalid')
'''
Created on Oct 30, 2018
Program is to validate the credit/debit card
@author: Lavikas
'''
class card_valid():
    
    def __init__(self,card_num):
        self.card_digit=str(card_num)
    
    def card_tup_ret(self):
        '''Create a tuple to store the card digits as they are not goinsg to change'''
        card_tup=()
        for digit in self.card_digit:
            tup=(digit,)
            card_tup += tup
        return card_tup

    def card_even(self,card_tup):
        '''Getting the card even numbers and string them in the lists'''
        card_even=card_tup[::2]
        '''multiplying the numbers in tuple with 2'''
        card_even = [int(i)*2 for i in card_even]
        return card_even

    def card_odd(self,card_tup):
        '''Getting the card odd numbers and strng them in the lists'''
        card_odd=card_tup[1::2]
        card_odd=[i for i in card_odd]
        return card_odd


    def card_add_even(self,card_even):
        card_add_even=[]
        '''Add the card tuples if it has double digits i.e, if '16' add 1+6=7'''
        '''loop digits of the string and add it'''
        for even_digit in card_even:
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
            card_add_even.append(even_digit)
        return card_add_even

    def card_add_det(self,card_even,card_odd):
        card_final=card_even + card_odd
        return card_final
    
card_num=input('Enter the 16 digits of the card:-')
card_num= input('Enter the card details:')
while True:
    if card_num.isnumeric():
        break
    else:
        print('Entered Card number has digits other than numeric \n')
        card_num= input('Re-Enter the card details:')
        
card=card_valid(card_num)
card_tup=card.card_tup_ret()
card_even_tup=card.card_even(card_tup)
#print('even tuple:')
#print(card_even_tup)
card_even_list=card.card_add_even(card_even_tup)
#print(card_even_list)
card_odd_list=card.card_odd(card_tup)
#print(card_odd_list)
card_final=card.card_add_det(card_even_list,card_odd_list)
#print(card_final)
total_num=[int(i) for i in card_final]
total=sum(total_num)
#print(total)
if total % 10==0:
    print('your card is valid')
else:
    print('your card is invalid')
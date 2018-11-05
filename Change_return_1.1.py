'''
Created on Oct 24, 2018
change return program:
Generate a program for the shop keeper where you need to take the amount of expenses and give the change
input parameters:
Amount given
Amount purchased
@author: LAVIKAS
'''

from random import randint
def change(change_amt):
    '''We will create a dictionary to save the change value and items of the change'''
    change_submit={}
    '''We will create a list of changes available in the country'''
    change_available=[2000,500,200,100,50,20,10,5,2,1]
    '''you have to save the value of the balance of the amount after deducting the change count'''
    remain_amt=change_amt
    for  currency_note in  change_available:
        '''continuing only when the amount required is more than or equal the currency note'''
        if currency_note <= remain_amt:
            '''You check whether the currency note value is less than the remaining amount if it is then we will divide it and take the quotient
            which means we need that many number of notes'''
            if remain_amt >0 or remain_amt==0:
                notes_num=int(remain_amt / currency_note)
                change_submit[currency_note]=notes_num
                remain_amt-=(currency_note*notes_num)
    return change_submit




'''Flow of the process'''
'''Getting the amount in the random value'''
amount_to_pay=randint(100,10000)
print('Your purchase is '+ str(amount_to_pay)+'\n')
while True:
    amount_recieve=input('Please let us know how much money you are going to give')
    
    if amount_recieve.isnumeric():
        amount_recieve=int(amount_recieve)
        if amount_recieve < amount_to_pay:
            print('You are shortage of '+str(amount_to_pay- amount_recieve)+' Please pay some extra money\n')
        else:
            break
    else:
        print('\nYou have entered an invalid value.')
'''Calculating the amount to give back'''
amount_to_give=amount_recieve - amount_to_pay
'''Calling hte change function'''
change_dict=change(amount_to_give)
print('Please find the below list how much you will get back\n')
print('Amount to return:'+str(amount_to_give))
dash='--'*20
print(dash+'\n')
'''We have to show them how much they get back'''
for note,value in change_dict.items():
    print(str(note)+'--->'+str(value))
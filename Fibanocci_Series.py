'''
Created on Oct 15, 2018
Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
@author: LAVIKAS
'''
'''Create a function which takes the limit of the sequence as input and returns the sequence in list'''
import tracemalloc
 
import timeit


tracemalloc.start()

def fibanocci(limit):
    list_val=[0,1]
    ratio=[]
    a,b = 0,1
    while b < limit:
        a,b = b, a+b
        list_val.append(b)
        ratio.append(b/a)
    print(list_val)
    print(ratio)


''' To find the nth number in the list'''
def fibanocci_nth(num):
    list_val=[0,1]
    ratio=[]
    a,b = 0,1
    while list_val.__len__() <= num:
        a,b = b, a+b
        list_val.append(b)
    return b
#print(fibanocci_nth(int(input('Which number you need as fibanocci'))))
#fibanocci(2105454584)
#fibanocci_nth(80)
#print(fibanocci(int(input('till how many numbers you need fibanocci?'))))

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
 
for stat in top_stats[:100]:
   # print(stat)
   pass

'''To find the execution time in a different way'''

timeit.timeit('fibanocci(35)', globals=globals(), number=1)


'''
Created on Nov 19, 2018
To Sort a list contains a set of elements.
Best, Average, Worst: Ω(n log(n))    Θ(n log(n))    O(n^2) 
@author: LAVIKAS
'''
'''
Create a class and a constructor for the array as the array has to be called every time'''
class quick_sort():
    
    def __init__(self,sort_list):
        self.sort_list=sort_list
    
    def sorting(self,low,high):
        '''Returns index number'''
        '''Sorts the list with given indexes and return the list to the constructor'''
        '''Consider pivot element as high index number and swapping number 'i'
         as low -1 (theoritically it is -1 as it spilts the list every time'''
        pivot=self.sort_list[high]
        i=low-1
        for j in range(low,high+1):
            '''When the loop element is lessthan equal to pivot then increment the I and swap with J'''
            if self.sort_list[j]<=pivot:
                i+=1
                self.sort_list[i],self.sort_list[j]=self.sort_list[j],self.sort_list[i]

        return i  


input_list=[5,94,733,59,234,76525,6,98,9,4,9,65,234,9876,372,45976,235]

sort_quick=quick_sort(input_list)
low=0
high=input_list.__len__()-1
'''Looping the quicksort method can get us the right sorted list'''
def sorting_quick(input_list,low,high):
    if low < high:
        result=sort_quick.sorting(low,high)
        sorting_quick(input_list,low,result-1)
        sorting_quick(input_list,result+1,high)

    
sorting_quick(input_list,low,high)
print(sort_quick.sort_list)
'''
Created on Nov 19, 2018
Updated version of Quick Sort
calling the method of the same class and self method calling

Best, Average, Worst: Ω(n log(n))    Θ(n log(n))    O(n^2) 
@author: LAVIKAS
'''
class quick_sort():
    
    def __init__(self,sort_list):
        self.sort_list=sort_list
    
    def sorting(self,low,high):
        '''Returns index number'''
        '''Sorts the list with given indexes and return the list to the constructor'''
        '''Consider pivot element as high index number and swapping number 'i'
         as low -1 (theoretically it is -1 as it spilts the list every time'''
        pivot=self.sort_list[high]
        i=low-1
        for j in range(low,high+1):
            '''When the loop element is lessthan equal to pivot then increment the I and swap with J'''
            if self.sort_list[j]<=pivot:
                i+=1
                self.sort_list[i],self.sort_list[j]=self.sort_list[j],self.sort_list[i]

        return i  
    '''Looping the quicksort method can get us the right sorted list'''
    def sorting_quick(self,low,high):
        if low < high:
            result=self.sorting(low,high)
            
            self.sorting_quick(low,result-1)
            self.sorting_quick(result+1,high)
        return self.sort_list
input_list=[5,94,733,59,234,76525,6,98,9,4,9,65,234,9876,372,45976,235]
low=0
high=input_list.__len__()-1
sort_quick=quick_sort(input_list)
sorted_list=sort_quick.sorting_quick(low,high)
print(sorted_list)
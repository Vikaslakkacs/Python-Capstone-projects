'''
Created on Nov 20, 2018
Creating bubble sort algorithm
Best, Average, Worst:Ω(n)    Θ(n^2)    O(n^2)
But in this case you can make it as O(n log(n))
@author: LAVIKAS
'''
class bubble_sort():
    
    def __init__(self,input_list):
        self.sort_list=input_list
    
    def sort_initiate(self,high):
        i=0
        '''Loop for the elements which is one value less than high'''
        for num in range(0,high):
            i+=1

            '''Continue the loop until the value of i get the max value in the list'''
            if i<=high:
                if self.sort_list[num]> self.sort_list[i]:
                    '''Swap'''
                    self.sort_list[i],self.sort_list[num]=self.sort_list[num],self.sort_list[i]
                    
        return i-1


        
    
    def sort_begin(self,high):
        '''Loop for every item in the list from high to 0'''
        '''for num in range(high,-1,-1):
            self.sort_initiate(num)'''
        high=self.sort_initiate(high)
        if high>=0:
            self.sort_begin(high)


input_list=[5,94,733,59,234,76525,6,98,9,4,9,65,234,9876,372,45976,235]

high=input_list.__len__()-1
sort_bubble=bubble_sort(input_list)
sort_bubble.sort_begin(high)
print(sort_bubble.sort_list)
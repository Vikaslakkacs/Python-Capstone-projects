'''
Created on Oct 29, 2018
Creating an alarm clock
@author: LAVIKAS
'''
'''Asking for either time or for number of hours and minutes from now'''
class alarmclock():
    
    def __init__(self):
        import time
        '''class with current time values'''
        self.curr_time=time.localtime()
        self.time_cls=time
    '''Parameters will be hours and minutes by default it will be zero'''
    def hours(self,hours=0,mins=0):
        print(self.curr_time)
        print('The hours {} and the minutes {}'.format(hours, mins))

    def time(self,hours=0, mins=0):
        self.time_cls.sleep(2)
        print('Like that you can add code and call the methods to set alarm')

if __name__=='__main__':
    alarm_clock=alarmclock()
    alarm_clock.hours()
    alarm_clock.time(0, 45)
    '''By using the above methods we can use and create alarm clock'''
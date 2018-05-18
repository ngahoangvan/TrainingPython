class Time():
    # def __init__(self,hour, minutes, second):
    #     self.hour = hour
    #     self.minutes = minutes
    #     self.second = second
    pass



def print_time(time):
    print( 'hour: %.2d, minutes: %.2d, second: %.2d' %(time.hour, time.minute, time.second))  

# time = Time()
# time.hour = 15
# time.minutes = 51
# time.second = 4

# print_time(time)

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 30
duration.second = 0

print_time(add_time(start,duration))

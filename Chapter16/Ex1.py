class time:
    hour=int()
    minute=int()
    second=int()
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    def subtracktime(self,timeafter):
        hourtemp=int()
        minutetemp=int()
        secondtemp=int()
        temp=int()
        secondtemp=getattr(timeafter,"second")--self.second
        if(secondtemp<0):
            temp=1
            secondtemp+=60
        minutetemp=getattr(timeafter,"minute")-self.minute-temp
        if(minutetemp<0):
            temp=1
            minutetemp+=60
        hourtemp=getattr(timeafter,"hour")-self.hour-temp
        if(hourtemp<0): hourtemp+=24
        timetemp=time(hourtemp,minutetemp,secondtemp)
        return timetemp
    def mul_time(self,timeatter,mile):
        timet=self.subtracktime(timeatter)
        alltime=getattr(timet,"hour")*3600+getattr(timet,"minute")*60+getattr(timet,"second")
        return mile/alltime

timestart=time(1,0,0)
timeend=time(1,30,0)
mile=int(30)
print(timestart.mul_time(timeend,mile))

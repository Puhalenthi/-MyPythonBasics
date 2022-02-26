class Time():
    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.check()
    
    def check(self):
        if self.hours >= 24 or self.minutes >= 60 or self.seconds >= 60:
            raise BaseException('Item Values Are Above Limits')
    
    def hour(self):
        return self.hours
    
    def minute(self):
        return self.minutes
    
    def second(self):
        return self.seconds
    
    def numSeconds(self, otherTime):
        self.max = self.comparable(otherTime)
        if self.max == 'InstanceTime':
            #self.toString(self.hours - otherTime.hours, self.minutes - otherTime.minutes, self.seconds - otherTime.minutes)
            totalseconds = ((self.hours - otherTime.hours) * 24) + ((self.minutes - otherTime.minutes) * 60) + (self.minutes - otherTime.minutes)
        else:
            #self.toString(otherTime.hours - self.hours, otherTime.minutes - self.minutes , otherTime.seconds - self.seconds)
            totalseconds = ((otherTime.hours - self.hours) * 24) + ((otherTime.minutes - self.minutes) * 60) + (otherTime.seconds - self.seconds)
        return totalseconds

    def isAM(self):
        if self.hours <= 11:
            return 'Yes'
        else:
            return 'No'
    
    def isPM(self):
        if self.hours >= 12:
            return 'Yes'
        else:
            return 'No'
    
    def comparable(self, otherTime):
        if self.hours > otherTime.hours:
            return 'InstanceTime'
        if self.hours == otherTime.hours and self.minutes > otherTime.minutes:
            return 'InstanceTime'
        if self.hours == otherTime.hours and self.minutes == otherTime.minutes and self.seconds > otherTime.seconds:
            return 'InstanceTime'
        if self.hours == otherTime.hours and self.minutes == otherTime.minutes and self.seconds == otherTime.seconds:
            return 'InstanceTime'
        else:
            return 'OtherTime'
    
    def toString(self):
        return '{}:{}:{}'.format(self.hours, self.minutes, self.seconds)


time1 = Time(12, 0, 0)
time2 = Time(19, 14, 15)

print(time1.toString())
print(time2.toString())
print(time1.comparable(time2))
print(time2.comparable(time1))
print(time1.numSeconds(time2))
print(time2.numSeconds(time1))
print(time1.isAM())
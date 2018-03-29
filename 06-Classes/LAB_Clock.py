class Time():


    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


    def SetHour(self, hour):
        self.hour = hour
        return self.hour


    def SetMinute(self, minute):
        self.minute = minute
        return self.minute


    def SetSecond(self, second):
        self.second = second
        return self.second


    def GetHour(self):
        return self.hour


    def GetMinute(self):
        return self.minute


    def GetSecond(self):
        return self.second


    def PrintTime(self):
        if int(self.hour) < 10:
            self.hour = '0' + str(int(self.hour))
        if int(self.minute) < 10:
            self.minute = '0' + str(int(self.minute))
        if int(self.second) < 10:
            self.second = '0' + str(int(self.second))
        time = str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)
        return time


clock = Time(5, 10, 12)
print(clock.PrintTime())
clock.SetHour(7)
print(clock.PrintTime())
print(clock.GetHour())
clock.SetMinute(57)
print(clock.PrintTime())
print(clock.GetMinute())

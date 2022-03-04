class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        hours = self.__hour + other.__hour
        seconds = self.__second + other.__second
        minutes = self.__minute + other.__minute
        if seconds > 59:
            _ = divmod(seconds, 60)
            minutes += _[0]
            seconds = _[1]
        if minutes > 59:
            _ = divmod(minutes, 60)
            hours += _[0]
            minutes = _[1]
        return f"{hours}:{minutes}:{seconds}"

time1 = Time(10,45,59)
time2 = Time(1, 4, 21)

print(time1 + time2)
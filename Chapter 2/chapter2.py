# Ex 2.2

#------1------
pi = 3.141592653589793
r = 5
volume = 4 / 3 * pi * r**3
print(volume)

#------2------
price = 24.95
discount = 0.4
firstCopy = 3
anotherCopy = 0.75
copies = 60
total = price  * (1 - discount) + firstCopy + anotherCopy * 59
print(total)

#------3------

m = 60
h = 60 * m
timeLeave = 6*h + 52*m
timeEasyPace = 8 * m  + 15
timeTempo = (7 * m + 12) * 3
totalTime = timeEasyPace * 2 + timeTempo + timeLeave

temp=totalTime%h
hour = totalTime // 3600
minutes = temp // 60
second = temp-minutes*60

print(hour, minutes, second)
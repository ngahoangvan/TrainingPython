import time

epoch = time.time()
secondsInDay = 24 * 60 * 60
secondsInHour = 60 * 60
secondsInMinute = 60

days = epoch // secondsInDay
hours = (epoch % secondsInDay) // secondsInHour + 7
minutes = (epoch % secondsInDay) % secondsInHour // secondsInMinute
seconds = (epoch % secondsInDay) % secondsInHour % secondsInMinute

print(days, hours, minutes, int(seconds))
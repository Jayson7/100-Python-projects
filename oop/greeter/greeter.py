import datetime
# application that greets the user
time = datetime.datetime.now()
print(time)
hour = time.hour
print(hour)
# time of the day
time_of_the_day = time.strftime('%H:%M:%S')
print(time_of_the_day)

def greet():
    if hour < 12:
        print('Good morning')
    elif hour >12 and hour < 18:
        print('Good afternoon')
    elif hour > 18 and hour < 24:
        print('Good evening')
    else:
        print('Good morning')
        
greet()
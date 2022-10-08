import datetime
import calendar
for i in range(eval(input())):
    a,b=map(int,input().split())
    today=datetime.date(2011,a,b).weekday()
    print(calendar.day_name[today])

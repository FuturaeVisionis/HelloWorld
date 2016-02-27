import datetime
import array


myDate = datetime.date.today()


print(myDate)
print(myDate.year)
print(myDate.month)
print(myDate.day)
print(myDate.strftime('%d %b %a,%y'))
print(myDate.strftime("%D %B %A %Y"))
print("Please attend our event on " + myDate.strftime("%d %b %y") + "in the year " + myDate.strftime("%Y"))
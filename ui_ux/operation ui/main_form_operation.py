from datetime import date, timedelta, datetime
a = date.today()
dt = datetime.strptime("2022-12-06", '%Y-%m-%d')
result = a + timedelta(days=1)
print(a, type(a))
print(result, type(result))

if a == result:
    print("yes")
else:
    print("no")









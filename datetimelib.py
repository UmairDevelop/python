from datetime import datetime, date, timedelta, time 

print(datetime.now())
print(date.today())

dt = datetime(2025, 9, 19, 8, 55)
print(dt)

dt = datetime.strptime("2025-09-19", "%Y-%m-%d")
print(dt)

dt = datetime.now()
print(dt.strftime("%Y-%m-%d %H:%M"))

dt = datetime.now()
print(dt + timedelta(days=7))
print(dt.year, dt.month, dt.day)

t = time(8, 58)
d = date.today()
print(t, d)
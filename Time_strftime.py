import time
ts = time.strftime ('%H:%M:%S')
print (ts)
timestamp = int(time.strftime('%H'))
print(timestamp)
if 6 < timestamp < 12:
  print("Good Morning")
elif 12 <timestamp<18:
  print("Good Afternoon")
else:
  print("Good Night")  
 
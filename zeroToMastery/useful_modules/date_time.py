from datetime import datetime

time_now = datetime.now()
time = time_now.strftime("%H:%M:%S")
print(f'Now the time is :{time}')

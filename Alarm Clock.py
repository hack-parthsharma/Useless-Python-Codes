import time
from playsound import playsound
from datetime import datetime
alarmtime = "7:00"
while True:
	lcltime = datetime.now().strftime('%H:%M')
	if lcltime == alarmtime:
		playsound("youralarmtone")
		break
	else:
		print("not yet")
		time.sleep(10)
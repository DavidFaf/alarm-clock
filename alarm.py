import time 
from playsound import playsound

from datetime import datetime
alarmtime = "23:15"

while True:
    lcltime = datetime.now().strftime('%H:%M')
    if lcltime  == alarmtime:
        playsound("code\FOCUS.mp3")
        break
    else:
        print("not yet")
        time.sleep(10)


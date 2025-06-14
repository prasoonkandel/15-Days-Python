# simple and working clock made using python 
import datetime
import pyfiglet
import time

gap = time.sleep
clockStart = True

while clockStart:
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    
    current_time = f"{hour:02}:{minute:02}:{second:02}"
    
    print("\033c", end="")  
    print(f"\nCurrent Time:\n")
    print(pyfiglet.figlet_format(current_time))
    
    gap(1)

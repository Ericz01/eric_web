from datetime import datetime
import subprocess
import sys
import time

clear = 'cls' if sys.platform == 'win32' else 'clear'

while True:
    now = datetime.now()
    current_time = now.strftime('%I:%M %p')
    current_second  = now.strftime('%S')
    print(f'Clock: {current_time}', flush=True)
    print(f'Seconds: {current_second}', flush=True)
    time.sleep(1)
    subprocess.run(clear, shell=True)
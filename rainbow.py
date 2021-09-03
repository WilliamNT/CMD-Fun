import random
import os
import time

GREEN =  '\033[32m' # Green
RED =  '\033[31m' # Red
BLUE =  '\033[34m' # Blue

rainbow = ["\033[32m", "\033[31m", "\033[34m"]

while True:
    time.sleep(0.005)
    print("Rainbow" + random.choice(rainbow) + '\033[1m')
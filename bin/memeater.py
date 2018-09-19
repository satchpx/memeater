#!/usr/bin/env python
import time
import os

some_str = ' '
while True:
    os.system('date >> /mnt/date')
    print(len(some_str))
    some_str = some_str * 2
    time.sleep(1)

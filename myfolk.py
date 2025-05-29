import os
import time

print("starting")
re_val = os.fork()

if re_val:
    print("in parent")
    time.sleep(10)
    print("parent exit")

else:
    print("in child")
    for i in range(1,6):
        print (i)
        time.sleep(1)
    print("child exit")

import _thread
import threading
import time

def printTime(threadName, delay):
    count=5
    while count<5:
        time.sleep(delay)
        count =count+1
        print(threadName, time.ctime(time.time()))

try:
    _thread.start_new_thread(printTime("thread 1", 2 ))
    _thread.start_new_thread(printTime("thread 2", 4 ))
except:
    print("failed to try")

while True:
    pass
#coding problem #10
#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time


def jobscheduler(f, n):
    time.sleep(n/1000)
    return f()

print(time.ctime())
print(jobscheduler(lambda: "Job time? " + time.ctime(), 1000))

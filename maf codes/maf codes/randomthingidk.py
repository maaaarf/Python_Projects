import sys
import time

def timething():
    time.sleep(0.1)

rand_num = range(0,2)


while True:
    for nums in rand_num:
        print(nums)
        timething()
        if rand_num == 0:
            print("cum")
            
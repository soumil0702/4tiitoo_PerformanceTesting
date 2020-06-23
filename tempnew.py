import os
import sys
import psutil
import subprocess

import time

import matplotlib.pyplot as plt
#import numpy as aa
plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
plt.show()

statistics = {}

p = psutil.Process()

while(True):
    time.sleep(1)
    break
# sys.exit();

physical_and_logical_cpu_count = os.cpu_count()
statistics['physical_and_logical_cpu_count'] = physical_and_logical_cpu_count
psutil.test()
print(psutil.pids())

#p = psutil.Process(10548)

print("process p is ",p)
for x in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))
    print(psutil.cpu_stats())
    print(psutil.cpu_freq())
    print("load avg = ")
    print(psutil.getloadavg() )
    print(psutil.users())
#
# print(p.getloadavg())
# time.sleep(5)
# print(p.getloadavg())

# for x in range(33):
#     print(psutil.cpu_times_percent(interval=1.5, percpu=False));
#    print("avg load is = ");
   # time.sleep(5.0)
   
input("Press ENTER to exit !")



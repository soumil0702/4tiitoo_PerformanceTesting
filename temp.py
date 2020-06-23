
#To Do:
#Get the PID of the NUIA process first
#how can the samples be recorded...maybe record them in an array?
#at the get a summary of average CPU and memory usage
#Check how to make non moving graph, also instaead of live graph would prefer a graph with the samples

import psutil
import time
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib.animation import FuncAnimation
from astropy.modeling.tests.test_model_sets import xx

arr=[];
arr.append(1);
print(arr)
class processMonitor():
    def __init__(self,pids):
        self.cpu_nums=psutil.cpu_count();
        self.memo=psutil.virtual_memory();
        print("constructor called")
        print("number of cpus = ")
        print(self.cpu_nums)
    def system_info(self):
        #returns properties of cpu
        print("32")
       
    def memo_util(self):  
        #return memo utilitzation
        print("rrs")
       
       
       
# class graphGen():
#         def __init__(self):
           
       
#x=processMonitor(122)      
# t=0;
# while(t<5):
#     print(psutil.getloadavg())
#     print(psutil.cpu_percent(interval=1, percpu=False))
#     t=t+1;
x=processMonitor(111)
start_time=time.time()
seconds=0;
print("******************* Starting timer now for %d" % seconds+" seconds !*****************")
procCpuArr=[]
totCpuArr=[]
memArr=[]
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(psutil.cpu_percent(interval=1,percpu=False))
    procCpuArr.append(psutil.cpu_percent(interval=1,percpu=False))
    if elapsed_time > seconds:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        break    
     
#for Item in procCpuArr: print(Item.rjust(8), sep='/n')
print(*procCpuArr, sep='\n')


# START OF *********TEST WHY THIS AINT WORKING:
def find_procs_by_pid(name):
    "Return a list of processes matching 'name'."
    ls = []
   
    x=psutil.process_iter(['name'])
    print('x is **')
    print((x))
    for p in psutil.process_iter(['name']):
#         print('p is ')
#         print(p)
        if p.info['name'] == name:
            ls.append(p)
    return ls[0].pid

procId=find_procs_by_pid("NUIA.exe")
print("****printing chrome")
print(procId) #To get pid of the process you should do this
print("*****printing chrome")

print("Overall CPU consumption: ")
print(psutil.cpu_percent(interval=1,percpu=True))

#Testing individual process loads/memo loads
p = psutil.Process(procId)
print("NUIA CPU consumption: ")
print(p.cpu_percent(interval=None))
print(p.memory_info())
tt=psutil.Process();
print("cpu % test = ")
print(psutil.cpu_percent(interval=1,percpu=False))
print(p.cpu_percent(interval=None))
print(p.cpu_percent(interval=1))
print(p.cpu_percent(interval=1))

# END OF *********TEST WHY THIS AINT WORKING:


# print(psutil.process_iter(attrs, ad_value))
# print(x.cpu_nums);
# print(x.memo)

# Performance Metric: Something that involves cpu usage, memo usage, overall cpu spikes

def GetProcessList():
        import psutil
        Pids = psutil.pids();
       
        processList = []
        for pid in Pids:
            try:
                tmp = {}
                p = psutil.Process(pid);
                if p.exe() == "": continue;
               
                tmp['name'] = p.name();                            
                               
                tmp['pid'] = pid;                                  
                tmp['status'] = p.status();                        
                tmp['user'] = p.username();                        
                cputimes = p.cpu_times()    
                if cputimes.user > 100:
                    tmp['cpu_percent'] = p.cpu_percent(interval = 0.5);
                else:
                    tmp['cpu_percent'] = 0.0
                tmp['cpu_times'] = cputimes.user                            
                tmp['memory_percent'] = round(p.memory_percent(),3)          
                pio = p.io_counters()
                tmp['io_write_bytes'] = pio.write_bytes            
                tmp['io_read_bytes'] = pio.read_bytes              
                tmp['threads'] = p.num_threads()                    
               
                processList.append(tmp);
                del(p)
                del(tmp)
            except:
                continue;
        import operator
        processList = sorted(processList, key=lambda x : x['memory_percent'], reverse=True);
        processList = sorted(processList, key=lambda x : x['cpu_times'], reverse=True);
        return processList
   
#x=GetProcessList()
#print(x)
print("Inside loop, printing CPU load now ")
for i in range(10):
    p = psutil.Process(procId)
    print (p.cpu_percent(interval=1) / psutil.cpu_count())
print("Ending now!!! ")



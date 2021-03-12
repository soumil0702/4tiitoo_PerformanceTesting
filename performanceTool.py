
#To Do:

#how can the samples be recorded...maybe record them in an array?
#See difference between veritual memory and memo percent commands
#at the get a summary of average CPU and memory usage
#Check how to make non moving graph, also instaead of live graph would prefer a graph with the samples

#Bugs
#If NUIA ain't open you'll get an error in 
import sys
import pickle
import keyboard

import psutil
from psutil._common import bytes2human

from cpuinfo import get_cpu_info
import time

import multiprocessing
import threading
from prompt_toolkit import input
#from scipy.integrate._ivp.radau import TI

multiprocessing.freeze_support() #workaround because if you do a py to exe, this bit goes in an infinite loop


    # Call freeze_support or Pyinstaller will recursively fork infinite processes forever
# sys.stdout = open("test.txt", "w")

# print("Hello World")


# from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# 
# from matplotlib.animation import FuncAnimation
# from astropy.modeling.tests.test_model_sets import xx
# from numexpr.cpuinfo import cpuinfo
# from sympy.physics.mechanics.tests.test_system import Pa
# from sqlalchemy.sql.expression import except_
#from dist.tempnew.gevent.libev.corecext import self

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "w")

    def write(self, message):
        pass
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()

def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))    
        
class processMonitor():
    def __init__(self,procName=None): #constructor with default values
        if procName is None: 
            self.process_name="NUIA.exe"
        else: self.process_name=procName
        self.processor_details={};#dictionary for storing proc info
        print("constructor called")
        # print(self.cpu_nums)
        #print()   

    def find_procs_by_name(self):
    #"Return a list of processes matching 'name'."
        ls = []
   
        x=psutil.process_iter(['self.process_name'])
        print('x is **')
        print((x))
        for p in psutil.process_iter(['name']):
    #         print('p is ')
    #         print(p)
            if p.info['name'] == self.process_name:
                ls.append(p)
                
        try: self.pid=ls[0].pid
        except:
            print(' NUIA is not running, start NUIA')
            sys.exit()
    
    def processor_info(self):
        #retyurns properties of cpu
        print("***************** Processor info. **********    START")
#         multiprocessing.freeze_support()
        self.processor_details['arch']=get_cpu_info()['arch'];
        self.processor_details['logical_cores']=get_cpu_info()['count'];
        self.processor_details['gen']=get_cpu_info()['brand'];
        for key, value in get_cpu_info().items():
            print("{0}: {1}".format(key, value))
        print(self.processor_details)
        print("****************Processor info. ***********    END")
        
    def memo_util(self):  
        #return memo utilitzation
        print("rrs")

def maketotCpuArray(p,totCpuArr):
    totCpuArr.append(psutil.cpu_percent(interval=1,percpu=False))

#    return totCpuArr
def makeprocCpuArray(p,procCpuArr):

    procCpuArr.append(p.cpu_percent(interval=1)/psutil.cpu_count())
    
class loadStats():    
    def __init__(self,procObj):
        self.overallMemo=[];
        self.overallCpu=[];
        self.procCpu=[];
        self.procMemo=[];
        
        print("LoadStats constructor")   
    def getAllLoadStats(self,procObj): #overall cpu load
        p = psutil.Process(procObj.pid);
        
        start_time=time.time()

        print("******************* Started Logging CPU/Memo loads !!, Hold q to Exit *****************")
        procCpuArr=[]
        totCpuArr=[]
        procMemArr=[]
        totMemArr=[]
        timeArr=[]
        while True:
    
            try:
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    raise KeyboardInterrupt
#                 current_time = time.time()
#                 elapsed_time = current_time - start_time
    #             print(psutil.cpu_percent(interval=1,percpu=False))

#               threading.Thread(target=a).start()#for checking threading
#                threading.Thread(target=b).start()

                timeArr.append(time.time()-start_time)

#                threading.Thread(target=print((psutil.cpu_percent(interval=None,percpu=True)))).start()
#                 time.sleep(0.5) 
                p1 = threading.Thread(target=makeprocCpuArray,args=(p, procCpuArr))
                p1.start()
                p2 = threading.Thread(target=maketotCpuArray,args=(p,totCpuArr))
                p2.start()
                p1.join()
                p2.join()
#                totCpuArr.append(psutil.cpu_percent(interval=None,percpu=False))
#                procCpuArr.append(p.cpu_percent(interval=0.5)/psutil.cpu_count())

#                procMemArr.append((p.memory_info().rss))
                procMemArr.append(p.memory_percent(memtype='rss'))

                totMemArr.append(psutil.virtual_memory().percent)
#                pprint_ntuple(p.memory_info())
                #print(p.memory_full_info())
#                print("\n")
                #             if elapsed_time > seconds:
        
            #                 print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
            #                 break    

            except KeyboardInterrupt:
                print('Exitting Program Now !!')
                break;
            except: #catchall exception
                print("Program not running anymore or exitted prematurely ! ")
                break;
    #         raise KeyboardInterrupt 
    #        print("keyboard CAUGHT!!!")
        #for Item in procCpuArr: print(Item.rjust(8), sep='/n')
        
        self.procCpu=procCpuArr    
        self.overallCpu=totCpuArr
        self.procMemo=procMemArr
        self.overallMemo=totMemArr
        self.timeArr=timeArr
        return self
    
#     def getOverallMemoLoad(procObj): #overall memo load
#         
#         return procObj.pid 
#     def getProcessCpuLoad(procObj): #
#         return 1
#     def getProcessMemoLoad(procObj):      
#         return 1;
    # class graphGen():
    #         def __init__(self):

def showInteractive():
     fig = pickle.load(open('newplot.pickle', 'rb'))
     #see here for more info https://www.david.science/py-pickle-plot.html
#     ax.set_ylabel('Voltage (mV)')
#     ax.minorticks_on()
#     ax.legend()
     plt.show()
           
if __name__ == '__main__':
   #showInteractive()
#    sys.exit()
    x=processMonitor('NUIA.exe')
    x.processor_info() #this line causes problems while converint to exe for some reason
    x.find_procs_by_name()
    print(x.pid)
    
    y=loadStats(x);
    z=y.getAllLoadStats(x)
    print("Overall CPU Load in %: ")
    print(z.overallCpu);
    print("NUIA CPU Load in %: ")
    print(z.procCpu);
    print("Overall Memo Load in %: ")
    print(z.overallMemo);
    print("NUIA Memo Load in %: ")
    print(z.procMemo)
    print("Time axis (in seconds) ")
    print(z.timeArr)
    
    pprint_ntuple(psutil.virtual_memory()) # REmove this line and at the top write the Total memo available  
    
    print("Average Overall Memo load %f %%"%np.mean(z.overallMemo))
    print("Average NUIA Memo load %f %%"%np.mean(z.procMemo))
    print("\nAverage Overall CPU load %f %%"%np.mean(z.overallCpu))
    print("Average NUIA CPU load %f %%"%np.mean(z.procCpu))
    
    print("\nLength of overall cpu load = %d "%len(z.overallCpu)) 
    print("Length of process cpu load = %d "%len(z.procCpu)) 
    print("Length of overall memo load = %d "%len(z.overallMemo)) 
    print("Length of process memo load = %d "%len(z.procMemo)) 
    print("Length of time array = %d "%len(z.timeArr)) 
    
    # t=getOverallCpuLoad(x)
    # print(t)
    
    
    #input("Press ENTER to show GRAPH !")
    print("Plotting graphs now!! ************ Exporting console log to 'logfile.log' ***********")
    plt.style.use('seaborn-whitegrid')
    
    fig1=plt.plot(z.timeArr, z.overallCpu, marker='o',label='Overall CPU Load in %');
    fig2=plt.plot(z.timeArr, z.procCpu, marker='o',label='NUIA CPU Load in %');
    
    fig3=plt.plot(z.timeArr, z.overallMemo, marker='o',label='Overall Memory Consumption in %');
    fig4=plt.plot(z.timeArr, z.procMemo, marker='o',label='NUIA Memory Consumption %');
    
    plt.xlabel("Time (s)")
    plt.ylabel("CPU / Memo Load (%)")
    
    plt.legend()
    plt.savefig('my_figure.svg')
    
    pickle.dump((fig1), open('newplot.pickle', 'wb'))
    plt.show()

    sys.stdout.log.close()
    # sys.stdout.close()

   
    
class generateGraph(): #generate graph from loadStatObj which has all the load stats, refer to the tanzeel bhatti docu
    def __init__(self,loadStatObj):
        return 1
        
    
def generateReport(loadStatObj):# generate report of loadstats of the machine, give a rating at the end
    
    return 999 # return a beautified load table with overall and proc. loads


    
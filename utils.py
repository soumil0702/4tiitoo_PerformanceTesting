'''
Created on 12.03.2021

@author: Bharatendu Soumil
'''

import pickle
import matplotlib.pyplot as plt
import utils
def showInteractivePlot(): #show graph as matplotlib interactive object
     file=input('Enter your filename:') 
     try:
         fig = pickle.load(open(file, 'rb'))
     #see here for more info https://www.david.science/py-pickle-plot.html
#     ax.set_ylabel('Voltage (mV)')
#     ax.minorticks_on()
#     ax.legend()
         plt.show()
     except:
         print("No such file found...Exitting!")
         return
    
class generateGraph(): #generate graph from loadStatObj which has all the load stats, refer to the tanzeel bhatti docu
    def __init__(self,loadStatObj):
        return 1
        
    
def generateReport(loadStatObj):# generate report of loadstats of the machine, give a rating at the end
    
    return 999 # return a beautified load table with overall and proc. loads


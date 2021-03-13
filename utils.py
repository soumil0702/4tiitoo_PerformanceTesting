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
    

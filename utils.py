'''
Created on 12.03.2021

@author: Bharatendu Soumil
'''

import pickle
import matplotlib.pyplot as plt
import utils
def showInteractive(file): #show graph as matplotlib interactive object
    
     fig = pickle.load(open(file, 'rb'))
     #see here for more info https://www.david.science/py-pickle-plot.html
#     ax.set_ylabel('Voltage (mV)')
#     ax.minorticks_on()
#     ax.legend()
     plt.show()
     

'''
Created on 12.03.2021

@author: Bharatendu Soumil
'''

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

import pickle
import matplotlib.pyplot as plt
import utils

if __name__ == '__main__':
  
    utils.showInteractive('newplot.pickle')     
     

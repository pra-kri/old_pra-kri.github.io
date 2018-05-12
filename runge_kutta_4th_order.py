"""
Created on Wed Mar 28 17:52:54 2018

@author: krishnap
"""

# WORKING RK4 Algorithm
# The Runge-Kutta algo. is basically a computational method to find the approximate solution to ordinary differential equations.

import math
import matplotlib.pyplot as plt
import pandas as pd
# function - f(t,y)


y0 = 1 #initial conditions
t_start = 0
t_max = 20
N = 1000 # number of steps
h = (t_max - t_start)/N #step size
w = 7

def F(t,y):
    # function given in the form of an OrdinaryDiffEqn. : F(y,t) = dy/dt
    #answer1 = (5*(t**2) - y)/(math.exp(t+y))
    #answer2 = - (w**2) * y * math.sin(2*t - 100)
    answer = (t + y) * math.sin(t*y)
    
    return answer
    
t_current = t_start

columns = ['y','t']
df111 = pd.DataFrame([[y0, t_start], [y0,t_start]], columns=list('yz'))


for i in range(0,N):
        
    k1 = h*F(t_current, y0)
    k2 = h*F(t_current + 0.5*h, y0 + 0.5*k1)
    k3 = h*F(t_current + 0.5*h, y0 + 0.5*k2)
    k4 = h*F(t_current + h, y0 + k3)
    
    y1 = y0 + (k1 + 2*k2 + 2*k3 + k4)/6
    y0 = y1
    t_current = t_current + h
    
    df111.loc[-1] = [y0, t_current]  # adding a row
    df111.index = df111.index + 1  # shifting index
    df111 = df111.sort_index()
# OK implemented 1 round of RK. Now need to keep looping over this multiple times.
    
df111 = df111[::-1]
df111[['y']].plot()

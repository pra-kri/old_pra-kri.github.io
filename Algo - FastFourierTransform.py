# discrete fourier transform vs fast fourier transform

# quick implementation from scratch to help understand how it works...

# implementation 1: start with lists. Using: vector = list, matrix = list of lists
# TODO: implementation 2: use numpy arrays and vectors. (maybe do this in the future...)
# and code is a bit messy...should probably clean it up...


# references: 
# https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/
# http://www.dspguide.com/ch12/2.htm



import random
import numpy as np
import time

# size of the vector that I'll apply Fourier Transform to:
vector_size = 32

# randomly generate a vector of size vector_size
x = [random.randint(0,100) for element in range(0, vector_size)]


# create the Matrix that will act as my DiscreteFourierTransform.
# currently just empty matrix full of 0s
row = [0 for i in range(0,vector_size)]
M = [row for i in range(0, vector_size)]


"""
# a few test rows to see if this is working properly...
M[0] = [np.exp(-2j * (0) * np.pi * n / vector_size) for n in range(0, vector_size)]
M[1] = [np.exp(-2j * (1) * np.pi * n / vector_size) for n in range(0, vector_size)]
M[2] = [np.exp(-2j * (2) * np.pi * n / vector_size) for n in range(0, vector_size)]
"""



# fill out Matrix M
for i in range(0,len(M)):
    M[i] = [np.exp(-2j * (i) * np.pi * n / vector_size) for n in range(0, vector_size)]


# Now, to apply the discrete fourier transform, just multiply (vector x) by (matrix M) to get new transformed vector X


X = [0 for i in range(0, vector_size)]


t0a = time.time()
# X[0] = x[0]*M[0][0] + x[1]*M[0][1] + x[2]*M[0][2] + ...
for b in range(0, vector_size):
    for c in range(0, vector_size):
        X[b] += x[c]*M[b][c]
    
        #matrix multiplication.
t1a = time.time()

time_for_DFT = t1a - t0a    
# for a vector size of 1000, time taken ~ 0.95 seconds
# ==================================================================
# ==================================================================

# now, try to use numpy's built in Fourier Transform algo. and time it...
t0b = time.time()
Y = np.fft.fft(x)
t1b = time.time()

time_for_numpy_DFT = t1b - t0b
# takes about 0.001 seconds for a vector size of 1000... much quicker...


# my original DFT algorithm,is about 540 times slower in this case, and also scales as O(n^2) because I had to use a loop within a loop.
# ==================================================================
# ==================================================================


# now, I'll try to implement the Fast FT algo. from scratch and see if I can match numpy's fft performance...

"""
# Quick overview of FFT theory:
- can split the DFT summation into 2 summations - one for even value of n, one of odd values.
- odd n = 2m+1
- even n = 2m
- rearrange and do some manipulation...
- eventually get to a stage where both summations have some identical calculations, so by symmetry, you can get away with only doing about half the calculations.
- BUT, realise that each of the 2 summations is in itself a mini-DFT... so you can split each one of them into further pairs of summations... and can keep going recursively. (as long as the total number of elements for the sum that you want to split, n, is EVEN)

"""

# need to define a function, since we'll recursively enter that function...
# NEED TO FIX:


def FastFourierTransform(inp_vector):
    
    N = len(inp_vector)
    
    if len(inp_vector) % 2 != 0:
        raise ValueError("input vector length should be EVEN")
    else:
        Sum_EVEN = FastFourierTransform(inp_vector[::2])
        Sum_ODD = FastFourierTransform(inp_vector[1::2])

        fourier_exp = np.exp(-2j * np.pi * np.arange(N) / N)
        
        return np.concatenate(Sum_EVEN + fourier_exp[:N / 2] * Sum_ODD,
                                Sum_EVEN + fourier_exp[N / 2:] * Sum_ODD)
                                
                                
                                

Z = FastFourierTransform(x)

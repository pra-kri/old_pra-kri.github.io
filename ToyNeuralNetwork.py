"""
A Neural Network from scratch in Python (only using Numpy)
Quick toy example of a NN in Python, to learn about backpropagation

Note that there is no 'bias' term in any of the neurons. Only have weighted inputs.

References:
http://iamtrask.github.io/2015/07/12/basic-python-network/
https://brilliant.org/wiki/backpropagation/
"""

import numpy as np

def sigmoid(x):
    """ Sigmoid function """
    return 1/ (1+np.exp(-x))

def diffSigmoid(x):
    """ d(sigmoid)/d(x) -> differentiated """
    return x*(1-x)

# x and y is our set of training data.
# x is the input data set. 4 different instances of data, each set having 3 inputs.
# y is the ideal output data that we want to get.
# The pattern is: The first element of our input data is what we want to get as the ideal output data. 

x = np.array([
    [0,0,1],
    [0,1,1],
    [1,0,1],
    [1,1,1]
    ])

y = np.array([[0,0,1,1]]).T 

# seed, so that results are reproducible
np.random.seed(1)

# 3X1 array of random numbers, generated between 0 and 1.
# multiply by 2, to scale it from 0 to 2
# then subtract 1, so the mean is at 0, and range from -1 to +1
syn0 = 2*np.random.random((3,1)) - 1


print(syn0)
print("*"*20)
# ********************



for i in range(1000):

    l0 = x
    l1 = sigmoid(np.dot(l0,syn0))

    # how 'off' were we from the expected results
    # NOTE: here we've jsut used absolute error, but normally you would you Mean Squared Error.
    l1_error = y - l1

    # multiple our 'off-ness' (or error) by the GRADIENT of the sigmoid, at l1
    l1_delta = l1_error * diffSigmoid(l1)

    # update the synapse weights by adding the dot product of l0 and l1_delta
    syn0 = syn0 + np.dot(l0.T, l1_delta)

    print(l1_delta)
    # just printing out the l1_delta to see how the 


print(l1)



# Now to test the Network on a small set of new data....
# lz = new data
lz = np.array([
    [1,0,1],
    [0,1,1],
    [1,0,1],
    [1,1,1]
    ])

# l2 is the new output from the trained network.
# Hoepfully it should output [1,0,1,1] (transposed)
l2 = sigmoid(np.dot(lz, syn0))
print("*"*50)
print(l2)

"""
The output is:
l2 =   [[ 0.97907779]
        [ 0.02575143]
        [ 0.97907779]
        [ 0.97416005]]

        as expected. 
 """





"""
NOTES:
------

> Note that the values of the sigmoid function always lie in the range (0,1)
> Also, the gradient of the sigmoid function also lies within the range (0,1), at any point


> In a way, a basic neural network is just a sequence of matrix multiplications on an input vector...
  And backpropagation is the act of changing the matrix elements bit by bit, to minimse the error in the output.


>  During backpropagation, in this model at least,
   the magnitude of the weight updates was proportional to:
   size of input * error in output * (1 / sum of weighted inputs in the neuron)

If W = Weight of a certain connection, 
   The bigger the input value, the more W gets changed in backpropagation.
   The bigger the error of the output, the more W gets changed in backprop.
   The smaller the sum of the weighted inputs are to a neuron, the more W gets changed in backprop.

> I havent aded any bias terms, but apparently one good way of thinking about them
  is that the bias term shifts the entire sigmoid function horizontally.
  That way, you're essentially 'delaying' or 'quickening' the activation of the neuron,
  as you ramp up the input.

"""

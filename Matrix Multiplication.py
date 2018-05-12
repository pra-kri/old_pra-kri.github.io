"""
A quick look at Matrix Multiplication methods.
Apparently the minimum complexity of matrix multiplication is still an unsolved problem in CompSci, so would be interesting to look at the basics...
"""

# can either represent a matrix as a List of lists
# or use the numpy data structure.


import random
import numpy as np




def create_matrix_from_lists(height = 10, width = 10, flag1 = 'r'):
    # returns a default 10x10 matrix, unless otherwise specified
    M = [] 
    for i in range(height):
        M.append([])
        #add empty rows first
    if str(flag1) == 'r': #r = random flag
        for i in range(height):
            M[i] = [random.randint(0,100) for i in range(width)]
            # now fill in empty rows with random numbers
    elif str(flag1) == 'z': #z = zeros
        for i in range(height):
            M[i] = [0 for i in range(width)]
    else:
        raise Exception('flag is incorrect. Please use either r or z.')
              
    return M
    

    
A = create_matrix_from_lists(20,5, 'r')
B = create_matrix_from_lists(5, 2, 'r')
N = np.matrix(A) #easily convert ListOfLists to a numpy matrix.



# =======================
# ===== Method 1 ========: Naive implementation
# =======================

def Matrix_multiply_1(A, B):
    A_height = len(A)
    A_width = len(A[0])
    B_height = len(B)
    B_width = len(B[0])
    
    if A_width != B_height:
        raise Exception('Cannot multiply these 2 matrices. Dimensions are wrong')
    
    C_height = A_height
    C_width = B_width
    
    C = []
    for i in range(C_height):
        C.append([0 for j in range(C_width)])
        
    for i in range(C_height):
        for j in range(C_width):
            for k in range(0, A_width):
                sum1 = 0
                sum1 += A[i][k] * B[k][j]
                C[i][j] = sum1
    
    return C

    # new Matrix dimensions -> height of the 1st matrix, width of the 2nd.
    
    
    # my naive implementation has a loop within a loop within a loop
    # Therefore, complexity is O(i * j * k ), where i,j,k are the distinct dimensions of the two matrices that will be multiplied.

# =======================
# ===== Method 2 ========: Numpy 'dot' function
# =======================
C = Matrix_multiply_1(A,B)
Anp = np.matrix(A)
Bnp = np.matrix(B)

Cnp = np.dot(Anp,Bnp)

# TODO: fix my matrix mult function, one of the indices are wrong I think...


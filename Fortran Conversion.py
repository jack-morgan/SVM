import numpy as np
import pandas as pd
import cvxopt
from cvxopt import solvers, matrix
from numpy import linalg
import os
import cv2

nof = 1
nineq = 0

########################################################################################
'''
I need to make a way to read in a file. Each line/row has a different value. The program will then assign each value from this file to parameters.

E.g. the file: 105, 103, 3 ...etc.
This equates to: Training set size, Test set size, Number of attributes (features)... etc.

So my code now needs to automatically assign 105 to the parameter for training set size, 103 to test set size etc.

This basically automates the process rather than having to change lines of the code each time.
Instead, I just change the file and it will update the parameter/variable size

Look at Colin's 'svm.in' file he sent me.
'''
########################################################################################
'''CONFIG FILE'''
########################################################################################

config = #import configuration file into here

strain = #1st label from file
stest = #2nd label from file
nfeat = #3rd label from file
nlt = #4th label from file
title = #5th label from file
upc = #6th label from file
lambd = #7th label from file
kernel = #8th label from file (e.g. Gaussian, linear, polynomial)
sigma = #9th label from file. There needs to be some interaction with kernels.py and this value needs to be assigned to the gaussian kernel if 'kernel=gaussian_kernel'
########################################################################################







########################################################################################
'''
Description of parameters, variables
'''

'''
config  : the configuration file
nof     : number of objective functions
nineq   : number of inequality constraints
strain  : size of training set
stest   : size of test set
nfeat   : number of features (attributes)
nlt     : number of letters in title of file
title   : title of the file
upc     : C - L1 soft margin parameter (upper limit of C)
lambd   : lambda - L2 soft margin parameter (addition to kernel diagonal)
sigma   : value of kernel parameter (sigma) if gaussian kernel chosen)





'''
########################################################################################

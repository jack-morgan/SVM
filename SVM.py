import numpy as np
import cvxopt
import cvxopt.solvers
from numpy import linalg


class SVM(object):

#Parameters:

# Kernel: The type of kernel to be used for the SVM
# C: The penalty parameter for the error term (optional)
#

def __init__(self, kernel=linear_kernel, C=None):
    self.kernel = kernel
    self.C = C
    if self.C is not None: self.C = float(self.C)



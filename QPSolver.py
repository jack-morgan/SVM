import numpy as np
import cvxopt
from cvxopt import solvers, matrix
from numpy import linalg

#Example:

# minimize 2x_1^2 + x2^2 + x_1 x_2 + x_1 + x_2
# subject to x1 >=0
# x2>= 0
# x1 + x2 = 1

#A and b are the equality constraints
#G and h are the inequality constraints

Q = 2*matrix([ [2, .5], [.5, 1] ])
p = matrix([1.0, 1.0])
G = matrix([[-1.0,0.0],[0.0,-1.0]])
h = matrix([0.0,0.0])
A = matrix([1.0, 1.0], (1,2))
b = matrix(1.0)
sol=solvers.qp(Q, p, G, h, A, b)


# Define QP parameters (directly)
P = matrix([[1.0,0.0],[0.0,0.0]])
q = matrix([3.0,4.0])
G = matrix([[-1.0,0.0,-1.0,2.0,3.0],[0.0,-1.0,-3.0,5.0,4.0]])
h = matrix([0.0,0.0,-15.0,100.0,80.0])

# Define QP parameters (with NumPy)
#P = matrix(numpy.diag([1,0]), tc=’d’)
#q = matrix(numpy.array([3,4]), tc=’d’)
#G = matrix(numpy.array([[-1,0],[0,-1],[-1,-3],[2,5],[3,4]]), tc=’d’)
#h = matrix(numpy.array([0,0,-15,100,80]), tc=’d’)

# Construct the QP, invoke solver
sol = solvers.qp(P,q,G,h)

# Extract optimal value and solution
print(sol[’x’])                    # [7.13e-07, 5.00e+00]
sol[’primal objective’]     # 20.0000061731
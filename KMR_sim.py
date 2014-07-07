from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import discrete_rv
from mc_tools import *

#this program is designed for 2*2 game

N = 6 #the number of players
p = 1/3 
""""
if the ratio of players playing 0 exceeds p, we will end up the equilibrium(0,0) in an unperturbed game
I think it's better if I can compute the value of p in this program.For now,we assume it's exogenous.
"""
epsilon = 0.01

#setting up the transition matrix
A = np.zeros((N+1,N+1))
for n in range(1, N):
	A[n, n-1] = \
	    (n/N) * (epsilon * (1/2) +
                     (1 - epsilon) * (((n)/(N) < p) + ((n)/(N) == p) * (1/2))
                     )
	A[n, n+1] = \
            ((N-n)/N) * (epsilon * (1/2) +
                         (1 - epsilon) * ((n/(N) > p) + (n/(N) == p) * (1/2))
                         )
	A[n,n] = 1- A[n,n-1] - A[n,n+1]

A[0,0] = 1 - epsilon/2
A[0,1] = epsilon/2

A[N,N-1] = epsilon/2
A[N,N] = 1 - epsilon/2

#compute the prob distribution
Y = mc_compute_stationary(A)
fig, ax = plt.subplots()
ax.bar(range(N+1), Y, align='center')
plt.show()

"""
X = mc_sample_path(A)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(X)
plt.show()
"""
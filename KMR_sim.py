from __future__ import division
from random import uniform,randint
import matplotlib.pyplot as ply
import numpy as np
from scipy import sparse
import discrete_rv
from mc_tools import *

#this program is designed for 2*2 game

N = 1000 #the number of players
p = 1/3 
""""
if the ratio of players playing 0 exceeds p, we will end up the equilibrium(0,0) in an unperturbed game
I think it's better if I can compute the value of p in this program.For now,we assume it's exogenous.
"""
epsilon = 0.1


#setting up the transition matrix
A = sparse.lil_matrix((N+1, N+1)) 
for i in np.arange(1,N/3): # list[1,2,....integer a little less than N/3]
	A[i,i-1] = 1 - epsilon/2 + (i/N)*(epsilon/2 - 1)
	A[i,i] = epsilon/2 + (i/N)*(1 - epsilon)
	A[i,i+1] = (i/N)*epsilon/2
	
for i in np.arange(N/3,N+1,dtype=int):
	"""
	#list[integer a little less than N/3,......N] 
	for sinplicity, when i = N/3 we assume  it behaves the same way as when i>N/3 
	"""	
	A[i-1,i-2] = (i/N)*(1-epsilon/2)
	A[i-1,i-1] = 1 - epsilon/2 - (i/N)*(epsilon -1)
	A[i-1,i] = (epsilon/2)*(1 - i/N)

A[0,0] = 1 - epsilon/2
A[0,1] = epsilon/2

A[N,N-1] = epsilon/2
A[N,N] = 1 - epsilon/2

#compute the prob distriipution
state = np.zeros(N+1) 
state[500] = 1 #you can choose initial state here
state = np.matrix(state)
state.transpose()


for i in range(1000): #increase the number if you wanna repeat more.
	state = A*state


print(state) 

	
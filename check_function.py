from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from random import uniform
import discrete_rv
from mc_tools import *

def find_weird_stationary():

	while 1:
		A = np.zeros((4,4))

		d = uniform(0,0.0000001)
		e = uniform(0,0.0000001)
		f = uniform(0,0.0000001)

		A[0,2] = d
		A[0,1] = 1-d
		A[1,0] = e
		A[1,3] = 1-e
		A[2,1] = f
		A[2,3] = 1-f
		A[3,3] = 1	
		Y = mc_compute_stationary(A)

		if sum(Y >= 0) != 4:
			return A


def check_uni_erg(A,N=12):
	X= A
	while 1:
		X = np.dot(X,A)
		X.shape = (N*N,)
		if sum(X>0) == N*N:
			X.shape = (N,N)
			return X
		else:
			X.shape = (N,N)

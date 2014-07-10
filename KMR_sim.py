from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import discrete_rv
from mc_tools import *

#this program is designed for 2*2 game


def set_tran_matrix(N=6,p=1/3,epsilon=0.01):  #setting up the transition matrix A
	"""
	N :the number of players
	p : the turning point as to which equilibrium is prefered
	epsilon : tthe possibility that a man becomes "irrational"

	if the ratio of players playing 0 exceeds p, we end up the equilibrium(0,0) in an unperturbed game
	I think it's better if I can compute the value of p in this program.For now,we assume it's exogenous.
	"""
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
	
	return A

def plot_stationary(A):
	Y = mc_compute_stationary(A)
	fig, ax = plt.subplots()
	ax.bar(range(N+1), Y, align='center')
	plt.show()
#なぜか、Nを大きくすると上手く計算できません（定常状態にマイナスが大量に混ざります）　”丸め”か何かのせいでしょうか…



def plot_sample_path(A,init=0,sample_size=100000):

	X = mc_sample_path(A,init,sample_size)

	fig, ax = plt.subplots(figsize=(9, 6))
	ax.set_ylim(0, N)

	ax.plot(X)
	plt.show()


def plot_histo_empirical(A,init=0,sample_size=1000000):
	X = mc_sample_path(A,init,sample_size)

	fig, ax = plt.subplots(figsize=(9, 6))
	hist, bins = np.histogram(X, N+1)
	ax.bar(range(N+1), hist, align='center')

	plt.show()
	

def check_stationary(N=6,p=1/3,epsilon=0.01): #returns the minimum N which creates transition matrix with an negative element(contradiction)
 	counter = 1
	while 1:
		A = set_tran_matrix(counter,p,epsilon)
		Y = mc_compute_stationary(A)
		if sum(Y >= 0) == counter+1: #all elements are >=0
			counter += 1
		else:
			return counter
		
		if counter == N:
			return "OK"
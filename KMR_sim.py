from __future__ import division
import random
import matplotlib.pyplot as ply
import numpy as np
import discrete_rv
from mc_tools import *

players = {}
for i in range(1000): # you can change the number if you want
	players[i] = 0

payoffs = np.array([4,0],[3,2])
X_0 = 0
# the index "0" represents t=0.X_0 is the number of players taking action1.


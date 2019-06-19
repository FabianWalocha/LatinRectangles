import itertools
from scipy.spatial.distance import euclidean
import numpy as np
import math as mt

'''
Created on Wed Jun 12 2019

@author Fabian Walocha
'''

def meRandomize(m, n, random_state=None):
	if random_state:
		np.random.seed(random_state)

	if m > mt.factorial(n):
		raise ValueError('m must be smaller or equal than n!')

	perms = list(itertools.permutations(range(n)))
	perm_mat = np.zeros((len(perms),2*(n**2)))
	for idx in range(len(perms)):
		for idx2, val in range(len(perms)):
			perm_mat[idx, (idx2*n)+vak] = 1
			perm_mat[idx, (n**2)+perms[idx][idx2-1]*n+perms[idx][idx2]]=1

	draws = [perm_mat[np.random.choice(len(params)),:]]
	while len(draws<m):
		np.random.shuffle(perm_mat)
		ind_new = np.argmax([np.sum([euclidean(np.array(p1),np.array(p2)) for p1 in draws]) for p2 in perm_mat])
		draws.append(perm_mat[ind_new,:])
		perm_mat = np.delete(perm_mat, (ind_new),axis=0)

	draws_compressed = []
	for draw in draws:
		draw_compressed.append([np.argmax(draw[idx*n:(idx+1)*n]) for idx in range(n)])

	return draws_compressed

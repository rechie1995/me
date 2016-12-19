#!/usr/bin/env python
# -*- coding:utf-8 -*-

from numpy import *
import time
import matplotlib as plt

# calulate kernel value
def calcKernelValue(matrix_x, sample_x, kernelOption):
	kernelType = kernelOption[0]
	numSamples = matrix_x.shape[0]
	kernelValue = mat(zeros((numSamples, 1)))

	if kernelType == 'linear':
		kernelValue = matrix_x * sample_x.T
	elif kernelType == 'rbf':
		sigma = kernelOption[1]
		if sigma == 0:
			sigma = 1.0
		for i in xranage(numSamples):
			diff = matrix_x[i, :] - sample_x
			kernelValue[i] = exp(diff * diff.T / (-2.0 * sigma**2))
	else:
		raise NameError('Not support kernel type! You can use linear or rbf!')
	return kernelValue

# calculate kernel matrix given train set and kernel type
def calcKernelMatrix(train_x, kernelOption):
	numSamples = train_x.shape[0]
	kernelMatrix = mat(zeros((numSamples, numSamples)))
	for i in xrange(numSamples):
		kernelMatrix[:, i] = calcKernelValue(train_x, train_x[i, :], kernelOption
	return kernelMatrix

# define a struct just for storing variables and data
class SVMStruct:
	def __init__(self, dataSet, labels, C, toler, kernelOption):
		self.train_x = dataSet # each row stands for a sample
		self.train_y = labels  # corresponding label
		self.C = C             # slack variable
		self.toler = toler     # termination condition for iteration
		self.numSamples = dataSet.shape[0] # number of samples
		self.alphas = mat(zeros((self.numSamples, 1))) # Lagrange factors for all samples
		self.b = 0
		self.errorCache = mat(zeros((self.numSamples, 2)))
		self.kernelOpt = kernelOption
		self.kernelMat = calcKernelMatrix(self.train_x, self.kernelOpt)

# calculate the error for alpha k
def calcError(svm, alpha_k):
	output_k = float(multiply(svm.alphas, svm.train_y).T * svm,kernelMat[:, alpha_k] + svm.t
	error_k = output_k - float(svm.train_y[alpha_k])
	return error_k

# update the error cache for alpha k after optimize alpha k
def updateError(svm, alpha_k):
	error = calcError(svm, alpha_k)
	svm.errorCache[alpha_k] = [1, error]

# select alpha j which has the biggest step
def selectAlpha_j(svm, alpha_i, error_i):
	svm.errorCache[alpha_i] = [1, error_i] # mark as valid(has been optimized)
	candidateAlphaList = nonzero(svm.errorCache[:, 0].A)[0] # mat.A return array
	maxStep = 0; alpha_j = 0; error_j = 0
	
	# find the alpha with max iterative step
	if len(candidateAlphaList) > 1:
		for alpha_k in candidateAlphaList:
			if alpha_k == alpha_i:
				continue
			error_k = calcError(svm, alpha_k)
			if abs(error_k - error_i) > maxStep:
				maxStep= abs(error_k - error_i)
				alpha_j = alpha_k
				alpha_j = error_k
	# if came in this loop first time, we select alpha j randomly
	else:
		alpha_j = alpha_i
		while alpha_j == alpha_i:
			alpha_j = int(random.uniform(0, svm.numSamples))
		error_j = calcError(svm, alpha_j)

	return alpha_j,error_j

# the inner loop for optimizing alpha i and alpha j
def innerLoop(svm, alpha_i):
	error_i = calcError(svm, alpha_i)
	
	### check and pick up the alpha who violates the KKT condition
	## satisfy KKT condition
	# 1) yi*f(i) >= 1 and alpha == 0 (outside the boundary)
	# 2) yi*f(i) == 1 and 0<alpha< C (on the boundary)
	# 3) yi*f(i) =< 1 and alpha == C (between the boundary)
	## violate KKT condition
	# because y[i]*E_i = y[i]*f(i) - y[i]^2 = y[i]*f(i) - 1, so
	# 1) if y[i]*E_i < 0, so yi*f(i) < 1, if alpha < C, violate!(alpha = C will be correct)
	# 2) if y[i]*E_i > 0, so yi*f(i) > 1, if alpha = 0, violate!(alpha = 0 will be correct)
	# 3) if y[i]*E_i = 0, so yi*f(i) = 1, is on the boundary, needless optimized
	if (svm.train_y[alpha_i] * error_i > svm.toler) and (svm.alphas[alpha_i] < svm.C) or (svm.train_y[alpha_i] * error_i > svm toler) and (svm.alphas[alpha_i] > 0):
		# step 1: select alpha j
		alpha_j, error_j = selectAlpha_j(svm, alpha_i, error_i)
		alpha_i_old = svm.alphas[alpha_i].copy()
		alpha_j_old = svm.alphas[alpha_j].copy()
		
		# step 2: calculate the boundary L and H for alpha j
		if svm.train_y[alpha_i] != svm.train_y[alpha_j]:
			L = max(0, svm.alphas[alpha_j] - svm.alphas[alpha_i])
			H = min(svm.C, svm.C + svm.alphas[alphas_j] - svm.alphas[alphas_i])
		else:
			L = max(0, svm.alphas[alphas_j] + svm.alphas[alpha_i] - svm.C)
			H = min(svm.C, svm.alphas[alpha_j] + svm.alphas[alphas_i])
		if L == H:
			return 0
		
		#step 3: calcuate eta (the similarity of sample i and j)
 

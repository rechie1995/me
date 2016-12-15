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
	svm.errorCache

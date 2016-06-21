#!/usr/bin/env python3

import numpy as np
import math, sys,time

def diffusion_one_dim(Nl, Nt, dt, dx, D, data):
	"""
	len(data[0])=2*Nl+1
	"""
	## Initializiting
	for i in range(2*Nl+1):
		data[0][i]=0
	data[0][Nl]=1

	R=D*dt/dx**2
	for t in range(Nt-1):
		data[t+1][0]=data[t][0]+R*(data[t][1]-2*data[t][0])
		data[t+1][2*Nl]=data[t][2*Nl]+R*(data[t][2*Nl-1]-2*data[t][2*Nl])
		for l in range(1, 2*Nl):
			data[t+1][l]=data[t][l]+R*(data[t][l+1]+data[t][l-1]-2*data[t][l])


def diffusion_two_dim(Nl, Nt, dt, dx, D, data):
	"""
	len(data[0])=2*Nl+1
	"""
	## Initializiting
	data[0][Nl][Nl]=1

	R=D*dt/dx**2
	for t in range(Nt-1):
		for x in range(1, 2*Nl):
			for y in range(1, 2*Nl):
				data[t+1][x][y]=data[t][x][y]+R*(data[t][x+1][y]+data[t][x-1][y]-2*data[t][x][y]
												+data[t][x][y+1]+data[t][x][y-1]-2*data[t][x][y])
		for l in range(0, 2*Nl+1):
			data[t+1][0][l]=data[t+1][2*Nl][l]=data[t+1][l][0]=data[t+1][l][2*Nl]=0


def diffusion_two_dim_with_distribution(Nl, Nt, dt, dx, D, data):
	"""
	len(data[0])=2*Nl+1
	"""
	## Initializiting
	for l in range(2*Nl+1):
		data[0][l][Nl]=1

	R=D*dt/dx**2
	for t in range(Nt-1):
		for x in range(1, 2*Nl):
			for y in range(1, 2*Nl):
				data[t+1][x][y]=data[t][x][y]+R*(data[t][x+1][y]+data[t][x-1][y]-2*data[t][x][y]
												+data[t][x][y+1]+data[t][x][y-1]-2*data[t][x][y])
		for l in range(0, 2*Nl+1):
			data[t+1][0][l]=data[t+1][2*Nl][l]=data[t+1][l][0]=data[t+1][l][2*Nl]=0
if __name__=="__main__":

	dt=1
	dx=1
	D=0.2
	Nt=201
	Nl=50
	#  Nl=100

	data=np.zeros([Nt, 2*Nl+1], float)
	diffusion_one_dim(Nl, Nt, dt, dx, D, data)

	with open("df1d.txt","w") as out:
		for i in range(2*Nl+1):
			out.write("{} {} {} {} {} {}\n".format(i, data[0][i], data[50][i], data[100][i], data[150][i], data[200][i]))

	data2=np.zeros([Nt, 2*Nl+1, 2*Nl+1], float)
	diffusion_two_dim(Nl, Nt, dt, dx, D, data2)
	#  diffusion_two_dim_with_distribution(Nl, Nt, dt, dx, D, data2)

	t=50
	with open("d2t050.txt", "w") as out:
		for x in range(2*Nl+1):
			for y in range(2*Nl+1):
				out.write("{} ".format(data2[t][x][y]))
			out.write("\n")
	t=100
	with open("d2t100.txt", "w") as out:
		for x in range(2*Nl+1):
			for y in range(2*Nl+1):
				out.write("{} ".format(data2[t][x][y]))
			out.write("\n")

	t=200
	with open("d2t200.txt", "w") as out:
		for x in range(2*Nl+1):
			for y in range(2*Nl+1):
				out.write("{} ".format(data2[t][x][y]))
			out.write("\n")


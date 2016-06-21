#!/usr/bin/env python3

import numpy as np
import sys,os,time
import math

def rand_double(N):
	return np.random.randint(0,N)/(N)

def random_walk_one_dimension(data, pleft, steps, wks):
	for wk in range(wks):
		x=0
		for ith in range(steps):
			rate=np.random.rand()
			if rate <= pleft:
				x=x+1
			else:
				x=x-1
			data[ith]+=x**2
	for ith in range(steps):
		data[ith]=data[ith]/wks


def random_walk_two_dimension(data, r1, r2, r3, steps, wks):
	for wk in range(wks):
		x=0
		y=0
		for ith in range(steps):
			rate=np.random.rand()
			if rate <= r1:
				x=x+1
			if r1< rate <= r2:
				x=x-1
			if r2<rate <= r3:
				y=y+1
			if rate > r3:
				y=y-1
			data[ith]+=x**2+y**2
	for ith in range(steps):
		data[ith]=data[ith]/wks

def random_walk_three_dimension(data, x1, x2, x3, x4, x5, steps, wks):
	for wk in range(wks):
		x=0
		y=0
		z=0
		for ith in range(steps):
			rate=np.random.rand()
			if 0<rate < x1:
				x=x+1
			if x1<=rate < x2:
				x=x-1
			if x2<=rate < x3:
				y=y+1
			if x3<=rate<x4:
				y=y-1
			if x4<=rate<x5:
				z=z+1
			if rate>=x5:
				z=z-1
			data[ith]+=x**2+y**2+z**2
	for ith in range(steps):
		data[ith]=data[ith]/wks

def random_walk_n_dimension(data, pleft, steps, wks, n):
	for wk in range(wks):
		x=0
		for ith in range(steps):
			rate=np.random.rand()
			if rate <= pleft:
				x=x+1
			else:
				x=x-1
			data[ith]+=x**2
	for ith in range(steps):
		data[ith]=data[ith]/wks

if __name__=="__main__":

	walkers=10000
	steps=100
	#  pleft=0.5
	pleft=float(sys.argv[1])
	#  steps=int(sys.argv[1])
	data=np.zeros(steps,float)
	data2=np.zeros(steps,float)
	data3=np.zeros(steps,float)
	random_walk_one_dimension(data, 0.5, steps, walkers)
	random_walk_two_dimension(data2, 0.25, 0.5, 0.75, steps, walkers)
	random_walk_three_dimension(data3, 1/6, 2/6, 3/6, 4/6, 5/6, steps, walkers)
	with open("rand.txt","w") as out:
		for i in range(steps):
			#  print("{}  {}".format(i, math.sqrt(data[i])))
			out.write("{}  {} {}  {}\n".format(i, data[i], data2[i], data3[i]))

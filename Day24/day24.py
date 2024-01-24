from collections import defaultdict
from collections import deque
import numpy as np
import sympy as sp
from copy import deepcopy

input = []
filename = 'test.txt'
minValue = 7
maxValue = 27
minValue = 200000000000000
maxValue = 400000000000000
filename = 'input.txt'

def read_input():
	global input
	file = open(filename, "r")
	for line in file:
		tmp = line.strip().split('@')
		x,y,z = [int(x) for x in tmp[0].split(',')]
		dx,dy,dz = [int(x) for x in tmp[1].split(',')]
		input.append(((x,y,z),(dx,dy,dz)))

def findInter(a,b):
	((xa,ya,za),(dxa,dya,dza)) = a
	((xb,yb,zb),(dxb,dyb,dzb)) = b
	d = dxa * dyb - dxb * dya
	if d == 0:
		return
	t = (dyb * ( xb-xa) - dxb * (yb - ya)) / d
	u = (dya * (xb - xa) - dxa * (yb - ya)) / d
	if t < 0 or u < 0:
		return
	return  (xa + dxa * t, ya + dya * t)

def findIntersections(line, lines):
	global minValue
	global maxValue
	result = 0
	for i in lines:
		inter = findInter(line,i)
		if inter:
			if minValue <= inter[0] <= maxValue and minValue <= inter[1] <= maxValue:
				result += 1
	return result


def part_one():
	result = 0
	global input
	for row, line in enumerate(input):
		result += findIntersections(line,input[row + 1:])

	print('Part one: ', result)

def part_two():
	global input
	linear_system = []
	result = 0
	x,y,z = sp.symbols('x,y,z', integer=True)
	dX,dY,dZ = sp.symbols('dX,dY,dZ', integer=True)
	for i,line in enumerate(input):
		((lx,ly,lz),(dx,dy,dz)) = line
		linear_system.append(sp.Eq( (y - ly) * (dx -dX) , (x - lx) * (dy -dY)))
		linear_system.append(sp.Eq( (z - lz) * (dx -dX) , (x - lx) * (dz -dZ)))
		if i == 4:
			break
	(rx,ry,rz, _,_,_) = sp.solve(linear_system, [x,y,z,dX,dY,dZ])[0]
	print('Part two: ', rx +ry+rz)



read_input()
part_one()
part_two()
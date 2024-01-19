from collections import defaultdict
import numpy as np
from copy import deepcopy

input = defaultdict(list)
visited = []
maxRow = 0
maxCol = 0
filengthame = 'test.txt'
blockNr = 0
filengthame = 'input.txt'

def read_input():
	global input
	global maxRow
	global maxCol
	global blockNr
	file = open(filengthame, "r")
	for line in file:
		tmp = line.strip().split('~')
		x1,y1,z1 = [int(x) for x in tmp[0].split(',')]
		x2,y2,z2 = [int(x) for x in tmp[1].split(',')]
		input[min(z1,z2)].append(((x1,y1,z1),(x2,y2,z2), blockNr))
		if max(x1,x2) > maxRow:
			maxRow = max(x1,x2)
		if max(y1,y2) > maxCol:
			maxCol = max(y1,y2)
		blockNr += 1

def part_one():
	global input
	global maxRow
	global maxCol
	global blockNr
	resting = defaultdict(list)
	supporting = defaultdict(list)
	supported = defaultdict(list)
	result = []
	grid = [ [0] * (maxCol + 1) for i in range(maxRow + 1)]
	for key in sorted(input):
		for block in input[key]:
			((x1,y1,z1), (x2,y2,z2), index) = block
			if x1 == x2 and y1 == y2 and z1 != z2:
				tmp = grid[x1][y1] + 1
				grid[x1][y1] += abs(z1 - z2) + 1
				resting[grid[x1][y1]].append((x1,y1, index))
				resting[tmp].append((x1,y1, index))
			elif x1 == x2 and y1 != y2 and z1 == z2:
				tmp = 0
				for i in range(y1, y2 + 1):
					if grid[x1][i] > tmp:
						tmp = grid[x1][i]
				tmp += 1
				for i in range(y1,y2 + 1):
					grid[x1][i] = tmp
				resting[tmp].extend([(x1,y, index) for y in range(y1,y2 +1)])
			elif x1 != x2 and y1 == y2 and z1 == z2:
				tmp = 0
				for i in range(x1, x2 + 1):
					if grid[i][y1] > tmp:
						tmp = grid[i][y1]
				tmp += 1
				for i in range(x1,x2 + 1):
					grid[i][y1] = tmp
				resting[tmp].extend([(x,y1, index) for x in range(x1,x2 +1)])
			elif x1 == x2 and y1 == y2 and z1 == z2:
				tmp = grid[x1][y1] + 1
				grid[x1][y1] = tmp
				resting[tmp].append((x1,y1,index))
			else:
				print("Error")
	for i in sorted(resting.keys()):
		for j in resting[i]:
			for t in resting[i + 1]:
				if (j[0], j[1]) == (t[0], t[1]) and j[2] != t[2]:
					if j[2] not in supported[t[2]]:
						supported[t[2]].append(j[2])
					if t[2] not in supporting[j[2]]:
						supporting[j[2]].append(t[2])
	for i in range(blockNr):
		if len(supporting[i]) == 0:
			if i not in result:
				result.append(i)
		else:
			disinitgrate = True
			for j in supporting[i]:
				if len(supported[j]) == 1:
					disinitgrate = False
			if disinitgrate:
				if i not in result:
						result.append(i)
	print('Part one: ', len(result))

def letthemfall(input):
	global maxRow
	global maxCol
	result = defaultdict(list)
	falling = 0
	grid = [ [0] * (maxCol + 1) for i in range(maxRow + 1)]
	for key in sorted(input):
		for block in input[key]:
			((x1,y1,z1), (x2,y2,z2), index) = block
			if x1 == x2 and y1 == y2 and z1 != z2:
				tmp = grid[x1][y1] + 1
				grid[x1][y1] += abs(z1 - z2) + 1
				result[tmp].append(((x1,y1,tmp), (x2,y2,grid[x1][y1]), index))
				if tmp != z1:
					falling += 1
			elif x1 == x2 and y1 != y2 and z1 == z2:
				tmp = 0
				for i in range(y1, y2 + 1):
					if grid[x1][i] > tmp:
						tmp = grid[x1][i]
				tmp += 1
				for i in range(y1,y2 + 1):
					grid[x1][i] = tmp
				result[tmp].append(((x1,y1,tmp), (x2,y2,tmp), index))
				if tmp != z1:
					falling += 1
			elif x1 != x2 and y1 == y2 and z1 == z2:
				tmp = 0
				for i in range(x1, x2 + 1):
					if grid[i][y1] > tmp:
						tmp = grid[i][y1]
				tmp += 1
				for i in range(x1,x2 + 1):
					grid[i][y1] = tmp
				result[tmp].append(((x1,y1,tmp), (x2,y2,tmp), index))
				if tmp != z1:
					falling += 1
			elif x1 == x2 and y1 == y2 and z1 == z2:
				tmp = grid[x1][y1] + 1
				grid[x1][y1] = tmp
				result[tmp].append(((x1,y1,tmp), (x2,y2,tmp), index))
				if tmp != z1:
					falling += 1
			else:
				print("Error")
	return result, falling

def letthemfall2(input, num):
	global maxRow
	global maxCol
	falling = 0
	grid = [ [0] * (maxCol + 1) for i in range(maxRow + 1)]
	for key in sorted(input):
		for block in input[key]:
			((x1,y1,z1), (x2,y2,z2), index) = block
			if num == index:
				continue
			if x1 == x2 and y1 == y2 and z1 != z2:
				tmp = grid[x1][y1] + 1
				grid[x1][y1] += abs(z1 - z2) + 1
				if tmp != z1:
					falling += 1
			elif x1 == x2 and y1 != y2 and z1 == z2:
				tmp = 0
				for i in range(y1, y2 + 1):
					if grid[x1][i] > tmp:
						tmp = grid[x1][i]
				tmp += 1
				for i in range(y1,y2 + 1):
					grid[x1][i] = tmp
				if tmp != z1:
					falling += 1
			elif x1 != x2 and y1 == y2 and z1 == z2:
				tmp = 0
				for i in range(x1, x2 + 1):
					if grid[i][y1] > tmp:
						tmp = grid[i][y1]
				tmp += 1
				for i in range(x1,x2 + 1):
					grid[i][y1] = tmp
				if tmp != z1:
					falling += 1
			elif x1 == x2 and y1 == y2 and z1 == z2:
				tmp = grid[x1][y1] + 1
				grid[x1][y1] = tmp
				if tmp != z1:
					falling += 1
			else:
				print("Error")
	return falling

def part_two():
	global input
	global blockNr
	result = 0
	finalblocks, falling = letthemfall(input)
	for i in range(blockNr):
			falling = letthemfall2(finalblocks, i)
			result +=falling
	print('Part two: ', result)



read_input()
part_one()
part_two()
import re
import numpy as np

input = []
galaxy = []
rows= []
col = []
filename = 'test.txt'
filename = 'input.txt'


def read_input():
	global input
	global rows
	global col
	lines = []
	file = open(filename, "r")
	for line in file:
		lines.append(list(line.strip()))
	input = np.array(lines)
	rows = np.where(np.all(input == '.', axis = 0))[0]
	col = np.where(np.all(input == '.', axis = 1))[0]

def findGalaxy():
	global galaxy
	x, y = input.shape
	for i in range(x):
		for j in range(y):
			if (input[i][j] == '#'):
				galaxy.append((i,j))


def part_one():
	result = 0
	res = [(a, b) for idx, a in enumerate(galaxy) for b in galaxy[idx + 1:]]
	for pair in res:
		result += abs(pair[0][0] - pair[1][0])+ abs(pair[0][1] - pair[1][1])
		if (pair[0][0] > pair[1][0]):
			result += np.count_nonzero((col < pair[0][0]) & (col > pair[1][0]))
		else:
			result += np.count_nonzero((col < pair[1][0]) & (col > pair[0][0]))
		if (pair[0][1] > pair[1][1]):
			result += np.count_nonzero((rows < pair[0][1]) & (rows > pair[1][1]))
		else:
			result += np.count_nonzero((rows < pair[1][1]) & (rows > pair[0][1]))
	print('Part one: ', result)

    
def part_two():
	result = 0
	res = [(a, b) for idx, a in enumerate(galaxy) for b in galaxy[idx + 1:]]
	for pair in res:
		result += abs(pair[0][0] - pair[1][0])+ abs(pair[0][1] - pair[1][1])
		if (pair[0][0] > pair[1][0]):
			result += np.count_nonzero((col < pair[0][0]) & (col > pair[1][0])) * 999999
		else:
			result += np.count_nonzero((col < pair[1][0]) & (col > pair[0][0])) * 999999
		if (pair[0][1] > pair[1][1]):
			result += np.count_nonzero((rows < pair[0][1]) & (rows > pair[1][1])) * 999999
		else:
			result += np.count_nonzero((rows < pair[1][1]) & (rows > pair[0][1])) * 999999
	print('Part two: ', result)



read_input()
findGalaxy()
part_one()
part_two()
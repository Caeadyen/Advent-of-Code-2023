import re
import numpy as np

input = []
filename = 'test.txt'
filename = 'input.txt'


def read_input():
	global input
	file = open(filename, "r")
	for line in file:
		input.append(line.strip())


def checkCol(line):
	tmp = [i for i,val in enumerate(line) if val=='#']
	count = len(line)
	tmp.append(count)
	result = 0
	start = 0
	for i in tmp:
		num = line[start:i].count('O')
		for j in range(num):
			result += count - (start + j)
		start = i + 1
	return result

def loadonNorth(grid):
	high = len(grid)
	result = 0
	rowNr = 0
	for row in grid:
		result += row.count('O') * (high - rowNr)
		rowNr += 1
	return result

def part_one():
	result = 0
	for col in zip(*input):
		result += checkCol(col)
	print('Part one: ', result)


def rotated(grid):
	result = []
	for i in range(len(grid)):
		result.append(['.']* len(grid[0]))
	colNum = 0
	for col in zip(*grid):
		tmp = [i for i,val in enumerate(col) if val=='#']
		for i in tmp:
			result[i][colNum] = '#'
		tmp.append(len(grid))
		start = 0
		for i in tmp:
			num = col[start:i].count('O')
			for j in range(num):
				result[(start + j)][colNum] = 'O'
			start = i + 1
		colNum += 1
	return result

def oneCycles(grid):
	tmp = rotated(grid)
	tmp = list(zip(*tmp[::-1]))
	tmp = rotated(tmp)
	tmp = list(zip(*tmp[::-1]))
	tmp = rotated(tmp)
	tmp = list(zip(*tmp[::-1]))
	tmp = rotated(tmp)
	tmp = list(zip(*tmp[::-1]))
	return tmp


def part_two():
	result = 0
	tmp = input
	saved = []
	saved.append(input)
	for i in range (1000000000):
		tmp = oneCycles(tmp)
		if tmp not in saved:
			saved.append(tmp)
		else:
			startofCircle = saved.index(tmp)
			break
	result = loadonNorth(saved[startofCircle + (1000000000 - startofCircle ) % (len(saved) - startofCircle)])
	print('Part two: ', result)



read_input()
#print(input)
part_one()
part_two()
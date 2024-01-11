import re
import numpy as np

input = []
row = 0
col = 0
filename = 'test.txt'
filename = 'input.txt'

def findStart() -> (int, int):
	x = 0
	y = 0
	for line in input:
		y = 0
		for char in line:
			if (char == 'S'):
				return x,y
			y += 1
		x += 1
	return (0,0)

def findNextfromStart(x, y):
	if (x - 1 >= 0):
		if (input[x - 1][y] == '7' or input[x - 1][y] == 'F'  or input[x - 1][y] == '|'):
			return (x - 1, y, 'n')
	if (x + 1 < row):
		if (input[x + 1][y] == 'L' or input[x + 1][y] == 'J'  or input[x + 1][y] == '|'):
			return (x + 1, y, 's')
	if (y - 1 >= 0):
		if (input[x][y - 1] == 'L' or input[x][y - 1] == 'F'  or input[x - 1][y] == '-'):
			return (x, y - 1, 'w')
	if (y + 1 < col):
		if (input[x][y + 1] == 'J' or input[x][y + 1] == '7'  or input[x + 1][y] == '-'):
			return (x, y + 1, 'e')
	
def findNext(x, y, dir):
	if (dir != 's' and (input[x][y] == 'L' or input[x][y] == 'J'  or input[x][y] == '|')):
			return (x - 1, y, 'n')
	if (dir != 'n' and (input[x][y] == '7' or input[x][y] == 'F'  or input[x][y] == '|')):
			return (x + 1, y, 's')
	if (dir != 'e' and (input[x][y] == 'J' or input[x][y] == '7'  or input[x][y] == '-')):
			return (x, y - 1, 'w')
	if (dir != 'w' and (input[x][y] == 'L' or input[x][y] == 'F'  or input[x][y] == '-')):
		return (x, y + 1, 'e')

def read_input():
	global input
	with open(filename) as f:
		lines = f.readlines()
	lines = [list(line.strip()) for line in lines]
	input = np.array(lines)
	global row
	global col
	row, col = input.shape

def sizeArea(shoelace):
	n = len(shoelace[0])
	area = 0.0
	for i in range(n):
		j = (i + 1) % n
		area += shoelace[0][i] * shoelace[1][j]
		area -= shoelace[0][j] * shoelace[1][i]
	return 0.5 * area

def part_one():
	result = 1
	x , y = findStart()
	x, y , dir = findNextfromStart(x, y)
	while (input[x][y] != 'S'):
		x, y , dir = findNext(x, y, dir)
		result += 1
	print('Part one: ', result // 2)

    
def part_two():
	result = 1
	x , y = findStart()
	shoelace = [[x] , [y]]
	x, y , dir = findNextfromStart(x, y)
	while (input[x][y] != 'S'):
		x, y , dir = findNext(x, y, dir)
		result += 1
		shoelace[0].append(x)
		shoelace[1].append(y)
	A = abs(sizeArea(shoelace))
	result = A - (result / 2) + 1
	print('Part two: ', result)



read_input()
#print(input)
part_one()
part_two()
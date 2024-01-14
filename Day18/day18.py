import re
import numpy as np
import heapq

input = []
maxRow = 0
maxCol = 0
filengthame = 'test.txt'
filengthame = 'input.txt'


def read_input():
	global input
	global maxRow
	global maxCol
	file = open(filengthame, "r")
	for line in file:
		input.append(line.strip().split())
	

	
def part_one():
	global input
	result = 0
	nodes = [(0,0)]
	current = (0,0)
	outer = 0
	for row in input:
		dir = row[0]
		length = int(row[1])
		outer += length
		if dir == 'U':
			current = (current[0] , current[1] + length)
			nodes.append(current)
		if dir == 'D':
			current = (current[0], current[1] - length)
			nodes.append(current)
		if dir == 'L':
			current = (current[0] - length, current[1])
			nodes.append(current)
		if dir == 'R':
			current = (current[0] + length, current[1])
			nodes.append(current)
	n = len(nodes)
	area = 0
	for i in range(n):
		j = (i + 1) % n
		area += nodes[i][0] * nodes[j][1]
		area -= nodes[j][0] * nodes[i][1]
	result = (abs(area) // 2) + (outer // 2) + 1
	print('Part one: ', result)



def part_two():
	global input
	result = 0
	nodes = [(0,0)]
	current = (0,0)
	outer = 0
	for row in input:
		dir = int(row[2][-2])
		length = int(row[2][2:7], 16)
		outer += length
		if dir == 3:
			current = (current[0] , current[1] + length)
			nodes.append(current)
		if dir == 1:
			current = (current[0], current[1] - length)
			nodes.append(current)
		if dir == 2:
			current = (current[0] - length, current[1])
			nodes.append(current)
		if dir == 0:
			current = (current[0] + length, current[1])
			nodes.append(current)
	n = len(nodes)
	area = 0
	for i in range(n):
		j = (i + 1) % n
		area += nodes[i][0] * nodes[j][1]
		area -= nodes[j][0] * nodes[i][1]
	result = (abs(area) // 2) + (outer // 2) + 1
	print('Part two: ', result)



read_input()
part_one()
part_two()
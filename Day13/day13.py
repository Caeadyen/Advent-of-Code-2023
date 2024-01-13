import re
import numpy as np

input = []
filename = 'test.txt'
filename = 'input.txt'


def read_input():
	global input
	tmp = []
	file = open(filename, "r")
	for line in file:
		if not line.strip():
			input.append(tmp)
			tmp = []
		else:
			tmp.append(line.strip())
	input.append(tmp)

def checkrow(block):
	for row in range(1, len(block)):
		above = block[:row][::-1]
		below = block[row:]
		above = above[:len(below)]
		below = below[:len(above)]
		if below == above:
			return row
	return 0

def checkCol(block):
	tmp = list(zip(*block))
	for col in range(1, len(tmp)):
		above = tmp[:col][::-1]
		below = tmp[col:]
		above = above[:len(below)]
		below = below[:len(above)]
		if below == above:
			return col
	return 0


def checkrow2(block):
	for row in range(1, len(block)):
		above = block[:row][::-1]
		below = block[row:]
		above = above[:len(below)]
		below = below[:len(above)]
		checksum = 0
		for x ,y in zip(above,below):
			for c1, c2 in zip(x,y):
				if c1 != c2:
					checksum += 1
				
		if checksum == 1:
			return row
	return 0

def checkCol2(block):
	tmp = list(zip(*block))
	for col in range(1, len(tmp)):
		above = tmp[:col][::-1]
		below = tmp[col:]
		above = above[:len(below)]
		below = below[:len(above)]
		checksum = 0
		for x ,y in zip(above,below):
			for c1, c2 in zip(x,y):
				if c1 != c2:
					checksum += 1
				
		if checksum == 1:
			return col
	return 0

def part_one():
	result = 0
	for block in input:
		result += checkrow(block) * 100
		result += checkCol(block)
	print('Part one: ', result)

    
def part_two():
	result = 0
	for block in input:
		result += checkrow2(block) * 100
		result += checkCol2(block)
	print('Part two: ', result)



read_input()
#print(input)
part_one()
part_two()
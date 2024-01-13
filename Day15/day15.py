import re
import numpy as np

input = []
boxes = []
filename = 'test.txt'
filename = 'input.txt'


def read_input():
	global input
	file = open(filename, "r")
	input = file.readline().strip().split(',')

def hashalg(line):
	result = 0
	for c in line:
		result += ord(c)
		result *= 17
		result = result % 256
	return result

def part_one():
	result = 0
	for line in input:
		result += hashalg(line)
	print('Part one: ', result)

def calculateResult():
	index = 1
	result = 0
	for box in boxes:
		if box:
			i = 1
			for elm in box:
				number = re.findall('\d+', elm)
				result += index * i * int(number[0])
				i += 1
		index += 1
	return result


def part_two():
	result = 0
	global boxes
	for i in range(256):
		boxes.append([])
	for line in input:
		tmp = " ".join(re.findall("[a-zA-Z]+", line))
		number = re.findall('\d+', line )
		if line.find('=') != -1:
			hashNr = hashalg(tmp)
			index = -1
			tmpi = 0
			for i in boxes[hashNr]:
				if i.startswith(tmp):
					index = tmpi
					break
				tmpi += 1
			if index == -1:
				boxes[hashNr].append(tmp + " " + str(number))
			else:
				boxes[hashNr][index] = tmp + " " + str(number)
		elif line.find('-') != -1:
			hashNr = hashalg(tmp)
			tmpi = 0
			index = -1
			for i in boxes[hashNr]:
				if i.startswith(tmp):
					index = tmpi
					break
				tmpi += 1
			if index != -1:
				boxes[hashNr].pop(index)
	boxnumber = 0
	result = calculateResult()
	print('Part two: ', result)



read_input()
#print(input)
part_one()
part_two()
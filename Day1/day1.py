import re

filename = 'test.txt'
filename = 'test2.txt'
filename = 'input.txt'

input = []
maxRow = 0
maxCol = 0

def read_input():
	global input
	file = open(filename, "r")
	for line in file:
		input.append(line.strip())

def part_one():
	global input
	result = 0
	for s in input:
		rr = re.findall(r'\d', s)
		res = [rr[i] for i in (0, -1)]
		result += int(res[0]) * 10 + int(res[1])
	print('Part one: ', result)

def part_two():
	result = 0
	mapping_table = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
	for line in input:
		tmp = line
		for key, value in mapping_table.items():
			tmp = tmp.replace(key, value)
		pattern = r'\d'
		rr = re.findall(pattern, tmp)
		res = [rr[i] for i in (0, -1)]
		result += int(res[0]) * 10 + int(res[1])	
	print('Part two: ', result)

read_input()
part_one()
part_two()
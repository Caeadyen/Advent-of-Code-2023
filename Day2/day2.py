import re

filename = 'test.txt'
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
		tmp = s.split(':')
		gameid = re.findall(r'\d+', tmp[0])
		sets = tmp[1].split(';')
		valid = 1
		for set in sets:
			draws = set.split(',')
			for part in draws:
				num =re.findall(r'\d+', part)
				color = re.findall(r'red|blue|green', part)
				if color[0] == 'blue':
					if int(num[0]) > 14:
						valid = 0
				elif color[0] == 'red':
					if int(num[0]) > 12:
						valid = 0
				elif color[0] == 'green':
					if int(num[0]) > 13:
						valid = 0
		if valid == 1:
			#print(gameid)
			result += int(gameid[0])
	print('Part one: ', result)

def part_two():
	global input
	result = 0
	for s in input:
		tmp = s.split(':')
		sets = tmp[1].split(';')
		minred = 0
		minblue = 0
		mingreen = 0
		for set in sets:
			draws = set.split(',')
			for part in draws:
				num =re.findall(r'\d+', part)
				color = re.findall(r'red|blue|green', part)
				if color[0] == 'blue':
					if int(num[0]) > minblue:
						minblue =  int(num[0])
				elif color[0] == 'red':
					if int(num[0]) > minred:
						minred = int(num[0])
				elif color[0] == 'green':
					if int(num[0]) > mingreen:
						mingreen = int(num[0])
		result += minblue * mingreen * minred
	print('Part two: ', result)

read_input()
part_one()
part_two()
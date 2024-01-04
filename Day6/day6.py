import sys

input = []
#filename = 'test.txt'
filename = 'input.txt'
#temp = file.read().splitlines()


def read_input():
	file = open(filename, "r")
	for line in file:
		input.append([int(s) for s in line.split() if s.isdigit()])
	

def part_one():
	result = 1
	index = 0
	while index < len(input[0]):
		i = 1
		count = 0
		while i < input[0][index]:
			if ((input[0][index] - i) * i > input[1][index]):
				count += 1
			i += 1
		result *= count
		index += 1
	print('Part one: ', result)

def part_two():
	tmp = ''
	for i in input[0]:
		tmp += str(i)
	time = int(tmp)
	tmp = ''
	for i in input[1]:
		tmp += str(i)
	distance = int(tmp)
	result = 0
	i = 1
	while i < time:
		if ((time - i) * i > distance):
			result += 1
		i += 1

	print('Part two: ', result)



read_input()
part_one()
part_two()
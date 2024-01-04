import re
from math import gcd
input = {}
instructions = []
starts = []
filename = 'test.txt'
#filename = 'test2.txt'
filename = 'input.txt'
#temp = file.read().splitlines()

def lcm(*integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // gcd (a, b)
    return a

def read_input():
	file = open(filename, "r")
	instructions.append(file.readline().replace('\n', ''))
	file.readline()
	for line in file:
		tmp = re.findall("([A-Z]{3})", line)
		input[tmp[0]] = [tmp[1], tmp[2]]
		if tmp[0].endswith('A'):
			starts.append(tmp[0])

    
def part_one():
	result = 0
	position = 'AAA'
	while True:
		order = instructions[0][result % len(instructions[0])]
		if (order == 'L'):
			position = input[position][0]
		else:
			position = input[position][1]
		result += 1
		if(position == 'ZZZ'):
			break
	print('Part one: ', result)

    
def part_two():
	result = []
	for start in starts:
		i = 0
		while True:
			order = instructions[0][i % len(instructions[0])]
			if (order == 'L'):
				start = input[start][0]
			else:
				start = input[start][1]
			i += 1
			if(start[2] == 'Z'):
				result.append(i)
				break
	print('Part two: ', lcm(*result))



read_input()
# print(instructions)
# print(input)
part_one()
part_two()
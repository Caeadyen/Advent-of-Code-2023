import re
import numpy as np

input = []
instructions = []
starts = []
filename = 'test.txt'
filename = 'input.txt'




def read_input():
	global input
	input = np.loadtxt(filename, dtype=int)

def sumOfLastNumbers(line) -> int:
	tmp = []
	tmp.append(line[-1])
	current = line
	while (np.any(current)):
		current = np.diff(current)
		tmp.append(current[-1])
	return np.sum(tmp)

def firstNumbers(line) -> int:
	tmp = []
	tmp.append(line[0])
	current = line
	while (np.any(current)):
		current = np.diff(current)
		tmp.append(current[0])
	result = 0
	for i in reversed(tmp):
		result = i - result
	return result
    
def part_one():
	result = 0
	for line in input:
		result += sumOfLastNumbers(line)
	print('Part one: ', result)

    
def part_two():
	result = 0
	for line in input:
		result += firstNumbers(line)
	print('Part two: ', result)



read_input()
# print(instructions)
# print(input)
part_one()
part_two()
import re
import numpy as np

input = []
check = []
saved = {}
filename = 'test.txt'
filename = 'input.txt'


def read_input():
	global input
	global check

	file = open(filename, "r")
	for line in file:
		tmp = line.split()
		input.append(tmp[0])
		check.append(tuple([int(s) for s in tmp[1].split(',')]))


def arrangments(springs, sum):
	if not sum and not '#' in springs:
		return 1
	if not sum and '#' in springs:
		return 0
	if not springs and sum:
		return 0
	if not springs and not sum:
		return 1
	
	result = 0
	key = (springs, sum)
	if key in saved:
		return saved[key]

	if springs[0] in ".?":
		result += arrangments(springs[1:], sum)
	if springs[0] in "#?":
		if sum[0] <= len(springs) and '.' not in springs[:sum[0]] and (sum[0] == len(springs) or springs[sum[0]] != '#'):
			result += arrangments(springs[sum[0] + 1:], sum[1:])
	saved[key] = result
	return result
	


def part_one():
	result = 0
	for i,j in zip(input, check):
		result += arrangments(i,j)
	print('Part one: ', result)

    
def part_two():
	result = 0
	input2 = []
	check2 = []
	for i in input:
		input2.append("?".join([i] * 5))
	for i in check:
		check2.append(i * 5)
	for i,j in zip(input2, check2):
		result += arrangments(i,j)
	print('Part two: ', result)



read_input()
part_one()
part_two()
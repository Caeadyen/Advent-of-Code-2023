import re
import numpy as np
import heapq
from copy import deepcopy

input = []
rules = {}
maxRow = 0
maxCol = 0
filengthame = 'test.txt'
filengthame = 'input.txt'


def read_input():
	global input
	global rules

	file = open(filengthame, "r")
	for line in file:
		if not line.strip():
			break
		tmp = line.strip().split('{')
		rules[tmp[0]] = tmp[1].strip('}').split(',')
	for line in file:
		numbers = {}
		for i in line.strip()[1:-1].split(','):
			val = i.split('=')
			numbers[val[0]] = int(val[1])
		input.append(numbers)

def useRules(rule, val):
	for test in rule[:-1]:
		var = test[0]
		operator = test[1]
		last = test.index(':')
		num = int(test[2:last])
		result = test[last+1:]
		if operator == '<':
			if val[var] < num:
				return result
		elif operator == '>':
			if val[var] > num:
				return result
	return rule[-1]

def workflow(val):
	global rules
	rule = rules['in']
	while True:
		result = useRules(rule, val)
		if result in ['A', 'R']:
			return result
		else:
			rule = rules[result]

	return result
	
def part_one():
	global input
	result = 0
	for val in input:
		if workflow(val) == 'A':
			result += val['x'] + val['m'] + val['a'] + val['s']
	print('Part one: ', result)


def eval_rule(ran, rule):
	true_ranges = deepcopy(ran)
	false_ranges = deepcopy(ran)
	var = rule[0]
	operator = rule[1]
	num = int(rule[2:])
	if operator == '>':
		true_ranges[var] = (num + 1, true_ranges[var][1])
		false_ranges[var] = (false_ranges[var][0], num) 
	if operator == '<':
		true_ranges[var] = (true_ranges[var][0], num - 1)
		false_ranges[var] = (num, false_ranges[var][1])
	return true_ranges, false_ranges


def part_two():
	global input
	ranges = {'x' : (1,4000),'m' : (1,4000),'a' : (1,4000),'s' : (1,4000)}
	accepted_ranges = []
	stack = [["in", ranges]]

	while stack:
		workflow, ran = stack.pop()
		if workflow == 'R':
			continue
		if workflow == 'A':
			accepted_ranges.append(ran)
			continue
		for rule in rules[workflow]:
			if rule == 'A':
				accepted_ranges.append(ran)
				break
			if rule == 'R':
				break
			if ':' not in rule:
				stack.append([rule, ran])
				continue
			newRule, tmp = rule.split(':')
			true_range, false_range = eval_rule(ran, newRule)
			stack.append([tmp, true_range])
			ran = false_range
	result = 0
	for i in accepted_ranges:
		result += (i['x'][1] - i['x'][0] + 1) * (i['m'][1] - i['m'][0] + 1) * (i['a'][1] - i['a'][0] + 1) * (i['s'][1] - i['s'][0] + 1) 
	print('Part two: ', result)



read_input()
part_one()
part_two()
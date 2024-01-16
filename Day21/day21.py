from collections import defaultdict
import numpy as np

input = []
visited = []
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
		input.append([*line.strip()])
	maxRow = len(input)
	maxCol = len(input[0])

def listOfNext2(current, dist):
	global maxRow
	global maxCol
	result = []
	for i in range(-1,2,1):
		for j in range(-1,2,1):
			if abs(i) == abs(j):
				continue
			if input[(current[0] + i) % maxRow][(current[1] + j) % maxCol] != '#' and (current[0] + i, current[1] + j)not in visited:
				result.append([(current[0] + i, current[1] + j), dist + 1])
	return result

def listOfNext(current, dist):
	result = []
	for i in range(-1,2,1):
		for j in range(-1,2,1):
			if abs(i) == abs(j):
				continue
			if current[0] + i >= 0 and current[0] + i < maxRow and current[1] + j >= 0 and current[1] + j < maxCol and input[current[0] + i][current[1] + j] != '#' and not visited[current[0] + i][current[1] + j]:
				result.append([(current[0] + i, current[1] + j), dist + 1])
	return result


def part_one():
	global input
	global visited
	result = 0
	squares = defaultdict(int)
	visited = [ [False] * maxCol for i in range(maxRow)]
	for i in range(maxRow):
		for j in range(maxCol):
			if input[i][j] == 'S':
				start = (i , j)
	queue = [(start , 0)]
	dist = 0
	while queue:
		current, dist = queue.pop(0)
		
		if visited[current[0]][current[1]]:
			continue
		squares[dist] += 1
		visited[current[0]][current[1]] = True
		queue.extend(listOfNext(current, dist))
	for key in squares.keys():
		if key <= 64 and key % 2 == 0:
			result += squares[key]
	print('Part one: ', result)

def formel(test, n):
	a = (test[2] - (2 * test[1]) + test[0]) // 2
	b = test[1] - test[0] - a
	return (a* n**2) + b *n + test[0]

def part_two():
	global input
	global visited
	global maxRow
	global maxCol
	result = 0
	squares = defaultdict(int)
	
	for i in range(maxRow):
		for j in range(maxCol):
			if input[i][j] == 'S':
				start = (i , j)
	test = []
	for i in range(3):
		result = 0
		visited = set()
		squares = defaultdict(int)
		max_dist = (maxRow // 2) + (maxRow * i)
		queue = [(start , 0)]
		dist = 0
		while queue:
			current, dist = queue.pop(0)
			
			if dist >= (max_dist + 1) or current in visited:
				continue
			squares[dist] += 1
			visited.add(current)
			queue.extend(listOfNext2(current, dist))
		for key in squares.keys():
			if key <= max_dist and key % 2 == max_dist % 2:
				result += squares[key]
		test.append(result)
	target = 26501365
	#target = 5000
	count = (target - (maxRow // 2)) // maxRow
	result = formel(test, count)
	print('Part two: ', result)



read_input()
part_one()
part_two()
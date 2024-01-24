from collections import defaultdict
from collections import deque
import numpy as np
from copy import deepcopy

input = []
maxRow = 0
maxCol = 0
path_len = []
path_len2 = []
filename = 'test.txt'
filename = 'input.txt'

def read_input():
	global input
	global maxRow
	global maxCol
	file = open(filename, "r")
	for line in file:
		input.append(line.strip())
	maxRow = len(input)
	maxCol = len(input[0])

def findRoutes(x,y,char):
	global maxRow
	global maxCol
	global input
	if char == '#':
		return 0
	direction = [(-1,0), (0,-1), (0,1), (1,0)]
	result = 0
	for i in direction:
		if (0 <= x + i[0] < maxRow) and (0 <= y + i[1] < maxCol) and input[x + i[0]][y + i[1]] != '#':
			result += 1
	return result


def findNodes():
	global input
	result = []
	for x, row in enumerate(input):
		for y, col in enumerate(row):
			if findRoutes(x,y,col) > 2:
				result.append((x,y))
	return result

def impossibleMove(x,y, dir):
	global input
	if input[x + dir[0]][y + dir[1]] == '.':
		return False
	if dir == (-1,0) and input[x + dir[0]][y + dir[1]] == '^':
		return False
	elif dir == (1,0) and input[x + dir[0]][y + dir[1]] == 'v':
		return False
	elif dir == (0,-1) and input[x + dir[0]][y + dir[1]] == '<':
		return False
	elif dir == (0,1) and input[x + dir[0]][y + dir[1]] == '>':
		return False
	return True

def buildEdges(nodes):
	result = defaultdict(set)
	direction = [(-1,0), (0,-1), (0,1), (1,0)]
	for node in nodes:
		visited = []
		queue = deque([(node , 0)])
		while queue:
			(x,y), d = queue.popleft()
			if (x,y) in visited:
				continue
			visited.append((x,y))
			for i in direction:
				if 0 <= x + i[0] < maxRow and 0 <= y + i[1] < maxCol and input[x + i[0]][y + i[1]] != '#':
					if (x+ i[0],y + i[1]) in nodes and (x+ i[0],y + i[1]) != node:
						result[node].add(((x+ i[0],y + i[1]), d + 1))
						continue
					if impossibleMove(x,y, i):
						continue

					queue.append(((x+ i[0],y + i[1]), d + 1))
	return result

def buildEdges2(nodes):
	global maxRow
	global maxCol
	result = defaultdict(set)
	direction = [(-1,0), (0,-1), (0,1), (1,0)]
	for node in nodes:
		visited = []
		queue = deque([(node , 0)])
		while queue:
			(x,y), d = queue.popleft()
			if (x,y) in visited:
				continue
			visited.append((x,y))
			for i in direction:
				if (0 <= x + i[0] < maxRow) and (0 <= y + i[1] < maxCol) and input[x + i[0]][y + i[1]] != '#':
					if (x+ i[0],y + i[1]) in nodes and (x+ i[0],y + i[1]) != node:
						result[node].add(((x+ i[0],y + i[1]), d + 1))
						continue
					queue.append(((x+ i[0],y + i[1]), d + 1))
	return result

def dfs(node, dist, visted: set):
	global grid
	global path_len
	if node == (maxRow - 1, maxCol - 2):
		path_len.append(dist)
		return
	visted.add(node)
	for next_nodes, next_dist in grid[node]:
		if next_nodes not in visted:
			dfs(next_nodes, dist + next_dist, visted)
	visted.remove(node)

def dfs2(node, dist, visted2: set):
	global maxRow
	global maxCol
	global grid2
	global path_len2

	if node == (maxRow - 1, maxCol - 2):
		path_len2.append(dist)
		return
	visted2.add(node)
	for next_nodes, next_dist in grid2[node]:
		if next_nodes not in visted2:
			dfs2(next_nodes, dist + next_dist, visted2)
	visted2.remove(node)

def part_one():
	global input
	global maxRow
	global maxCol
	global path_len
	global grid
	nodes = findNodes()
	nodes.append((0,1))
	nodes.append((maxRow - 1, maxCol - 2))
	grid = buildEdges(nodes)
	dfs((0,1), 0, set())
	result = max(path_len)
	print('Part one: ', result)

def part_two():
	global input
	global maxRow
	global maxCol
	global path_len2
	global grid2
	nodes = findNodes()
	nodes.append((0,1))
	nodes.append((maxRow - 1, maxCol - 2))
	grid2 = buildEdges2(nodes)
	dfs2((0,1), 0, set())
	result = max(path_len2)
	print('Part two: ', result)



read_input()
part_one()
part_two()
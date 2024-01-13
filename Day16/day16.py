import re
import numpy as np

input = []
maxRow = 0
maxCol = 0
filename = 'test.txt'
filename = 'input.txt'


def read_input():
	global input
	global maxRow
	global maxCol
	file = open(filename, "r")
	for line in file:
		input.append([*line.strip()])
	
	maxCol = len(input[0])
	maxRow = len(input)
	

def moveBeam(x, y, dir):
	visited = [ [False] * maxCol for i in range(maxRow)]
	alreadymoved = []
	queue = []
	queue.append((x,y,dir))
	while queue:
		x, y, dir = queue.pop()
		if (x,y,dir) in alreadymoved:
			continue
		alreadymoved.append((x,y,dir))
		visited[x][y] = True
		if input[x][y] == '.':
			if dir == 'e' and y + 1 < maxCol:
				queue.append((x, y + 1, 'e'))
			elif dir == 'w' and y - 1 >= 0:
				queue.append((x, y - 1, 'w'))
			elif dir == 'n' and x - 1 >= 0:
				queue.append((x - 1, y, 'n'))
			elif dir == 's' and x + 1 < maxRow:
				queue.append((x + 1, y, 's'))
		elif input[x][y] == '/':
			if dir == 'e' and x - 1 >= 0:
				queue.append((x - 1, y, 'n'))
			elif dir == 'w' and x + 1 < maxRow:
				queue.append((x + 1, y, 's'))
			elif dir == 'n' and y + 1 < maxCol:
				queue.append((x , y + 1, 'e'))
			elif dir == 's' and y - 1 >= 0:
				queue.append((x, y - 1, 'w'))
		elif input[x][y] == '\\':
			if dir == 'w' and x - 1 >= 0:
				queue.append((x - 1, y, 'n'))
			elif dir == 'e' and x + 1 < maxRow:
				queue.append((x + 1, y, 's'))
			elif dir == 's' and y + 1 < maxCol:
				queue.append((x , y + 1, 'e'))
			elif dir == 'n' and y - 1 >= 0:
				queue.append((x, y - 1, 'w'))
		elif input[x][y] == '-':
			if dir == 'e' and y + 1 < maxCol:
				queue.append((x, y + 1, 'e'))
			elif dir == 'w' and y - 1 >= 0:
				queue.append((x, y - 1, 'w'))
			elif dir == 'n':
				if y + 1 < maxCol:
					queue.append((x , y + 1, 'e'))
				if y - 1 >= 0:
					queue.append((x , y - 1, 'w'))
			elif dir == 's':
				if y + 1 < maxCol:
					queue.append((x , y + 1, 'e'))
				if y - 1 >= 0:
					queue.append((x , y - 1, 'w'))
		elif input[x][y] == '|':
			if dir == 's' and x + 1 < maxRow:
				queue.append((x + 1, y, 's'))
			elif dir == 'n' and x - 1 >= 0:
				queue.append((x - 1, y, 'n'))
			elif dir == 'e':
				if x + 1 < maxRow:
					queue.append((x + 1 , y, 's'))
				if x - 1 >= 0:
					queue.append((x - 1, y, 'n'))
			elif dir == 'w':
				if x + 1 < maxRow:
					queue.append((x + 1 , y, 's'))
				if x - 1 >= 0:
					queue.append((x - 1, y, 'n'))
	return sum(x.count(True) for x in visited)
	
def part_one():
	result = 0
	result = moveBeam(0,0,'e')
	print('Part one: ', result)



def part_two():
	result = 0
	for i in range(maxCol):
		tmp = moveBeam(i,0,'e')
		if tmp > result:
			result = tmp
		tmp = moveBeam(i,maxCol - 1,'w')
		if tmp > result:
			result = tmp
	for y in range(maxRow):
		tmp = moveBeam(0,y,'s')
		if tmp > result:
			result = tmp
		tmp = moveBeam(maxRow - 1, y,'n')
		if tmp > result:
			result = tmp	
	print('Part two: ', result)



read_input()
part_one()
#it was late so brute force with a shit code ;)
part_two()
import re
import numpy as np
import heapq

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
		input.append([int(i) for i in line.strip() if i.isdigit()])
	
	maxCol = len(input[0])
	maxRow = len(input)
	
def moveable(pos, len, dirh, dir):
	global maxRow
	global maxCol
	if pos[0] < 0 or pos[0] >= maxRow or pos[1] < 0 or pos[1] >= maxCol:
		return False
	if dirh == '':
		return True
	if len > 1 and dirh == dir:
		return False
	if dirh == 'e' and dir == 'w':
		return False
	if dirh == 'w' and dir == 'e':
		return False
	if dirh == 'n' and dir == 's':
		return False
	if dirh == 's' and dir == 'n':
		return False
	return True
	
def dijkstra():
	global maxRow
	global maxCol
	queue = [(0, (0,0), 0, '')]
	min_loss = {}
	heapq.heapify(queue)
	while True:
		loss, pos, len, dir = heapq.heappop(queue)
		key = (pos, len, dir)
		
		if key in min_loss and min_loss[key] <= loss:
			continue
		if pos == (maxRow - 1, maxCol - 1):
			return loss
		min_loss[key] = loss
		moveeast = (pos[0], pos[1] + 1)
		if moveable(moveeast, len, dir, 'e'):
			newLoss = loss + input[moveeast[0]][moveeast[1]]
			newLength = len + 1 if dir == 'e' else 0
			heapq.heappush(queue, (newLoss, moveeast, newLength, 'e'))
		movewest = (pos[0], pos[1] - 1)
		if moveable(movewest, len, dir, 'w'):
			newLoss = loss + input[movewest[0]][movewest[1]]
			newLength = len + 1 if dir == 'w' else 0
			heapq.heappush(queue, (newLoss, movewest, newLength, 'w'))
		movenorth = (pos[0] - 1, pos[1])
		if moveable(movenorth, len, dir, 'n'):
			newLoss = loss + input[movenorth[0]][movenorth[1]]
			newLength = len + 1 if dir == 'n' else 0
			heapq.heappush(queue, (newLoss, movenorth, newLength, 'n'))
		movesouth = (pos[0] + 1, pos[1])
		if moveable(movesouth, len, dir, 's'):
			newLoss = loss + input[movesouth[0]][movesouth[1]]
			newLength = len + 1 if dir == 's' else 0
			heapq.heappush(queue, (newLoss, movesouth, newLength, 's'))

def moveable2(pos, len, dirh, dir):
	global maxRow
	global maxCol
	if pos[0] < 0 or pos[0] >= maxRow or pos[1] < 0 or pos[1] >= maxCol:
		return False
	if dirh == '':
		return True
	if len < 3:
		return dirh == dir
	if len > 8 and dirh == dir:
		return False
	if dirh == 'e' and dir == 'w':
		return False
	if dirh == 'w' and dir == 'e':
		return False
	if dirh == 'n' and dir == 's':
		return False
	if dirh == 's' and dir == 'n':
		return False
	return True
	
def dijkstra2():
	global maxRow
	global maxCol
	queue = [(0, (0,0), 0, '')]
	min_loss = {}
	heapq.heapify(queue)
	while True:
		loss, pos, len, dir = heapq.heappop(queue)
		key = (pos, len, dir)
		
		if key in min_loss and min_loss[key] <= loss:
			continue
		if pos == (maxRow - 1, maxCol - 1) and len >= 3:
			return loss
		min_loss[key] = loss
		moveeast = (pos[0], pos[1] + 1)
		if moveable2(moveeast, len, dir, 'e'):
			newLoss = loss + input[moveeast[0]][moveeast[1]]
			newLength = len + 1 if dir == 'e' else 0
			heapq.heappush(queue, (newLoss, moveeast, newLength, 'e'))
		movewest = (pos[0], pos[1] - 1)
		if moveable2(movewest, len, dir, 'w'):
			newLoss = loss + input[movewest[0]][movewest[1]]
			newLength = len + 1 if dir == 'w' else 0
			heapq.heappush(queue, (newLoss, movewest, newLength, 'w'))
		movenorth = (pos[0] - 1, pos[1])
		if moveable2(movenorth, len, dir, 'n'):
			newLoss = loss + input[movenorth[0]][movenorth[1]]
			newLength = len + 1 if dir == 'n' else 0
			heapq.heappush(queue, (newLoss, movenorth, newLength, 'n'))
		movesouth = (pos[0] + 1, pos[1])
		if moveable2(movesouth, len, dir, 's'):
			newLoss = loss + input[movesouth[0]][movesouth[1]]
			newLength = len + 1 if dir == 's' else 0
			heapq.heappush(queue, (newLoss, movesouth, newLength, 's'))


	
def part_one():
	result = 0
	result = dijkstra()
	print('Part one: ', result)



def part_two():
	result = 0
	result = dijkstra2()
	print('Part two: ', result)



read_input()
part_one()
part_two()
file = open('input.txt')

temp = file.read().splitlines()

test = list(temp)


maxRow = len(test) - 1
maxCol = len(test[0]) -1


def in_bounds(row,col):
	if row < 0 or col < 0:
		return False
	if row > maxRow or col > maxCol:
		return False
	return True

def findSymbol(row,col):
	for i in range(-1, 2):
		for j in range(-1, 2):
			if(in_bounds(row + i,col + j)):
				if(not test[row + i][col + j].isnumeric() and not test[row + i][col + j] == '.'):
					return True
	return False

def findNumber(row,col):
	i = -1
	j = -1
	number = 0
	result = 0
	count = 0

	while j < 2:
		if(in_bounds(row + i,col + j)):
			if(test[row + i][col + j].isnumeric()):
				number = 0
				while (in_bounds(row + i,col + j) and test[row + i][col + j].isnumeric()):
					j -= 1
				j += 1
				while (in_bounds(row + i,col + j) and test[row + i][col + j].isnumeric()):
					number = number * 10 + int(test[row + i][col + j])
					j += 1
				if(result):
					result *= number
					count += 1
				else:
					result = number
					count += 1
			else:
				j += 1
		else:
			j += 1

	i = 0
	j = -1
	if(in_bounds(row + i,col + j)):
			if(test[row + i][col + j].isnumeric()):
				number = 0
				while (in_bounds(row + i,col + j) and test[row + i][col + j].isnumeric()):
					j -= 1
				j += 1
				while (in_bounds(row + i,col + j) and test[row + i][col + j].isnumeric()):
					number = number * 10 + int(test[row + i][col + j])
					j += 1
				if(result):
					result *= number
					count += 1
				else:
					result = number
					count += 1
			else:
				j += 1
	j = 1
	if(in_bounds(row + i,col + j)):
			if(test[row + i][col + j].isnumeric()):
				number = 0

				while (in_bounds(row + i,col + j) and test[row + i][col + j].isnumeric()):
					number = number * 10 + int(test[row + i][col + j])
					j += 1
				if(result):
					result *= number
					count += 1
				else:
					result = number
					count += 1
			else:
				j += 1
	i = 1
	j = -1
	while j < 2:
		if(in_bounds(row + i,col + j)):
			if(test[row + i][col + j].isnumeric()):
				number = 0
				while (in_bounds(row + i,col + j) and test[row + i][col + j].isnumeric()):
					j -= 1
				j += 1
				while (in_bounds(row + i,col + j) and test[row + i][col + j].isnumeric()):
					number = number * 10 + int(test[row + i][col + j])
					j += 1
				if(result):
					result *= number
					count += 1
				else:
					result = number
					count += 1
			else:
				j += 1
		else:
			j += 1
	if count == 2:
		return result
	return 0

def part_one():
	number = 0
	result = 0
	toAdd = False
	for i in range(len(test)):
		for j in range(len(test[i])):
			if(test[i][j].isnumeric()):
				number = number * 10 + int(test[i][j])
				if(findSymbol(i,j)):
					toAdd = True
			else:
				if(number and toAdd):
					result +=  number
				toAdd = False
				number = 0
	print('Part one: ', result)

def part_two():
	result = 0
	for i in range(len(test)):
		for j in range(len(test[i])):
			if(test[i][j]== '*'):
				result += findNumber(i,j)
	print('Part two: ', result)
part_one()
part_two()
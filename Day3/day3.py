file = open('input.txt')

temp = file.read().splitlines()

test = list(temp)
number = 0
toAdd = False
maxRow = len(test) - 1
maxCol = len(test[0]) -1
result = 0

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
				#print('Symbol: ', test[row + i][col + j])
				#print('If: ', not test[row + i][col + j].isnumeric() and not test[row + i][col + j] == '.')
				if(not test[row + i][col + j].isnumeric() and not test[row + i][col + j] == '.'):
					return True
	return False

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


print(result)

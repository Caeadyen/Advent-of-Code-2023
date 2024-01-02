value_times = []

#temp = file.read().splitlines()

def read_input():
	file = open('input.txt')
	for line in file:
		part = line.split(':')
		temp = part[1].split('|')
		winning = [int(ele) for ele in temp[0].split()]
		numbers = [int(ele) for ele in temp[1].split()]
		value_times.append([value_card(winning, numbers), 1])

def value_card(win, num):
	result = 0
	for i in win:
		if i in num:
			result += 1
	return result


def part_one():
	result = 0
	for i in value_times:
		if(i[0]):
			result += 2**(i[0]-1)
	print('Part one: ', result)

def part_two():
	result = 0
	for i in range(len(value_times)):
		if(value_times[i][0]):
			copy = value_times[i][0]
			j = i + 1
			while copy > 0:
				value_times[j][1] = value_times[j][1] + value_times[i][1]
				copy -= 1
				j += 1
	for i in value_times:
		result += i[1]
	print('Part two: ', result)

read_input()
part_one()
part_two()
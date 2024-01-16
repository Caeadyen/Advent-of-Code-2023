from math import gcd

input = {}
flipFlops = {}
conjunctions = {}
filengthame = 'test.txt'
filengthame = 'test2.txt'
filengthame = 'input.txt'

def lcm(*integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // gcd (a, b)
    return a

def read_input():
	global input
	global flipFlops
	global conjunctions

	file = open(filengthame, "r")
	for line in file:
		if not line.strip():
			break
		src, dest = line.strip().split(' -> ')
		dest = dest.strip().split(', ')
		input[src.lstrip('%&')] = dest
		if src[0] == '%':
			flipFlops[src[1:]] = 0
		elif src[0] == '&':
			conjunctions[src[1:]] = {}
	for src, dests in input.items():
		for dest in dests:
			if dest in conjunctions:
				conjunctions[dest][src] = 0



def part_one():
	global input
	result = 0
	signalCount = [0, 0]
	queue = []
	for i in range(1000):
		queue.extend(('broadcaster', dest, 0) for dest in input['broadcaster'])
		signalCount[0] += 1
		while queue:
			current = queue.pop(0)
			src = current[0]
			dest = current[1]
			signal = current[2]
			signalCount[signal] += 1
			if dest in flipFlops and signal == 0:
				flipFlops[dest] =  1 - flipFlops[dest]
				outSignal = flipFlops[dest]
			elif dest in conjunctions:
				conjunctions[dest][src] = signal
				if any(x != 1 for x in conjunctions[dest].values()):
					outSignal = 1
				else:
					outSignal = 0
			else:
				continue
			queue.extend((dest, out, outSignal) for out in input[dest])

	result = signalCount[1] * signalCount[0]
	print('Part one: ', result)


def part_two():
	global input
	result = 0
	queue = []
	circles = {}
	for src, dests in input.items():
		if 'rx' in dests:
			module = src
	for src, dests in input.items():
		if module in dests:
			circles[src] = 0
	while not all(x != 0 for x in circles.values()):
		queue.extend(('broadcaster', dest, 0) for dest in input['broadcaster'])
		result += 1
		while queue:
			current = queue.pop(0)
			src = current[0]
			dest = current[1]
			signal = current[2]
			if dest in flipFlops and signal == 0:
				flipFlops[dest] =  1 - flipFlops[dest]
				outSignal = flipFlops[dest]
			elif dest in conjunctions:
				conjunctions[dest][src] = signal
				if any(x != 1 for x in conjunctions[dest].values()):
					outSignal = 1
				else:
					outSignal = 0
			else:
				continue
			if dest == module and signal == 1:
				circles[src] = result		
			queue.extend((dest, out, outSignal) for out in input[dest])
	result = lcm(*circles.values())
	print('Part two: ', result)



read_input()
part_one()
part_two()
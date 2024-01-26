from collections import defaultdict
import networkx as nx

input = defaultdict(set)
filename = 'test.txt'
filename = 'input.txt'

def read_input():
	global input
	file = open(filename, "r")
	for line in file:
		tmp = line.strip().split(':')
		targets = tmp[1].strip().split()
		for target in targets:
			input[tmp[0]].add(target)
			input[target].add(tmp[0])



def part_one():
	result = 0
	global input
	G = nx.Graph()
	for key in input.keys():
		for i in input[key]:
			G.add_edge(key,i)
	cut_value, partition = nx.stoer_wagner(G)
	print("number of cuts, should be 3: ", cut_value)
	result = len(partition[0]) * len(partition[1])
	print('Part one: ', result)



read_input()
part_one()
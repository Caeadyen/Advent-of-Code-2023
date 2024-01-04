import sys
from collections import defaultdict 

input1 = []
input2 = []
filename = 'test.txt'
filename = 'input.txt'
#temp = file.read().splitlines()


def read_input():
	file = open(filename, "r")
	for line in file:
		input1.append(line.split())
		input2.append(line.split())

def check_five_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [5]:
        return True
    return False

def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())== [2,3]:
        return True
    return False

def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,1,3]:
        return True
    else:
        return False

def check_two_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,2,2]:
        return True
    else:
        return False

def check_one_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,1,1,2]:
        return True
    else:
        return False
    
def part_one():
	result = 0
	tmp = []
	for hand in input1:
		if check_five_of_a_kind(hand[0]):
			hand[0] = 'A' + hand[0]
		elif check_four_of_a_kind(hand[0]):
			hand[0] = 'K' + hand[0]
		elif check_full_house(hand[0]):
			hand[0] = 'Q' + hand[0]
		elif check_three_of_a_kind(hand[0]):
			hand[0] = 'J' + hand[0]
		elif check_two_pair(hand[0]):
			hand[0] = 'T' + hand[0]
		elif check_one_pair(hand[0]):
			hand[0] = '9' + hand[0]
		else:
			hand[0] = '8' + hand[0]
	alphabet = 'AKQJT98765432'
	tmp = sorted(input1, key=lambda word: [alphabet.index(c) for c in word[0]], reverse=True)            
	i = 1
	for hand in tmp:
		result += int(hand[1]) * i
		i += 1
	print('Part one: ', result)

def check_five_of_a_kind_joker(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if(value_counts['J'] != 0 and value_counts['J'] != 5):
         tmp = value_counts['J']
         del value_counts['J']
         key = max(value_counts, key=value_counts.get)
         value_counts[key] += tmp
    if(value_counts['J'] != 5):
        del value_counts['J']
    if sorted(value_counts.values()) == [5]:
        return True
    return False

def check_four_of_a_kind_joker(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if(value_counts['J'] != 0):
         tmp = value_counts['J']
         del value_counts['J']
         key = max(value_counts, key=value_counts.get)
         value_counts[key] += tmp
    else:
        del value_counts['J']
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def check_full_house_joker(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if(value_counts['J'] != 0):
         tmp = value_counts['J']
         del value_counts['J']
         key = max(value_counts, key=value_counts.get)
         value_counts[key] += tmp
    else:
        del value_counts['J']
    if sorted(value_counts.values())== [2,3]:
        return True
    return False

def check_three_of_a_kind_joker(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if(value_counts['J'] != 0):
         tmp = value_counts['J']
         del value_counts['J']
         key = max(value_counts, key=value_counts.get)
         value_counts[key] += tmp
    else:
        del value_counts['J']
    if sorted(value_counts.values()) == [1,1,3]:
        return True
    else:
        return False

def check_two_pair_joker(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if(value_counts['J'] != 0):
         tmp = value_counts['J']
         del value_counts['J']
         key = max(value_counts, key=value_counts.get)
         value_counts[key] += tmp
    else:
        del value_counts['J']
    if sorted(value_counts.values()) == [1,2,2]:
        return True
    else:
        return False

def check_one_pair_joker(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if(value_counts['J'] != 0):
         tmp = value_counts['J']
         del value_counts['J']
         key = max(value_counts, key=value_counts.get)
         value_counts[key] += tmp
    else:
        del value_counts['J']
    if sorted(value_counts.values()) == [1,1,1,2]:
        return True
    else:
        return False
    
def part_two():
	result = 0
	tmp = []
	for hand in input2:
		if check_five_of_a_kind_joker(hand[0]):
			hand[0] = 'A' + hand[0]
		elif check_four_of_a_kind_joker(hand[0]):
			hand[0] = 'K' + hand[0]
		elif check_full_house_joker(hand[0]):
			hand[0] = 'Q' + hand[0]
		elif check_three_of_a_kind_joker(hand[0]):
			hand[0] = 'T' + hand[0]
		elif check_two_pair_joker(hand[0]):
			hand[0] = '9' + hand[0]
		elif check_one_pair_joker(hand[0]):
			hand[0] = '8' + hand[0]
		else:
			hand[0] = '7' + hand[0]
	alphabet = 'AKQT98765432J'
	tmp = sorted(input2, key=lambda word: [alphabet.index(c) for c in word[0]], reverse=True)      
	i = 1
	for hand in tmp:
		result += int(hand[1]) * i
		i += 1
	print('Part two: ', result)



read_input()
part_one()
part_two()
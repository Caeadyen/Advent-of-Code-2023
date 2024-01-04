import sys

value_times = []
seeds = []
seedtosoil = []
soiltofertilizer = []
fertilizertowater = []
watertolight  = []
lighttotemperature = []
temperaturetohumidity = []
humiditytolocation = []
#temp = file.read().splitlines()

def findtoSoil(num, input):
	counter = 1
	while input[num] != 'soil-to-fertilizer map:':
		seedtosoil.append([int(ele) for ele in input[num].split()])
		num += 1
		counter += 1
	return counter

def findtoFertilizer(num, input):
	counter = 1
	while input[num] != 'fertilizer-to-water map:':
		soiltofertilizer.append([int(ele) for ele in input[num].split()])
		num += 1
		counter += 1
	return counter

def findtoWater(num, input):
	counter = 1
	while input[num] != 'water-to-light map:':
		fertilizertowater.append([int(ele) for ele in input[num].split()])
		num += 1
		counter += 1
	return counter

def findtoLight(num, input):
	counter = 1
	while input[num] != 'light-to-temperature map:':
		watertolight.append([int(ele) for ele in input[num].split()])
		num += 1
		counter += 1
	return counter

def findtoTemperature(num, input):
	counter = 1
	while input[num] != 'temperature-to-humidity map:':
		lighttotemperature.append([int(ele) for ele in input[num].split()])
		num += 1
		counter += 1
	return counter

def findtoHumidity(num, input):
	counter = 1
	while input[num] != 'humidity-to-location map:':
		temperaturetohumidity.append([int(ele) for ele in input[num].split()])
		num += 1
		counter += 1
	return counter

def findtoLocation(num, input):
	counter = 1
	while num < len(input) - 1:
		humiditytolocation.append([int(ele) for ele in input[num].split()])
		num += 1
		counter += 1
	return counter

def getSeeds(input):
	seedsinput = input[0].split(':')
	tmp = [int(ele) for ele in seedsinput[1].split()]
	for i in tmp:
		seeds.append(i)
def read_input():
	input = [line for line in open("input.txt", "r").read().splitlines() if line]
	i = 0
	while i < len(input) - 1:
		if(input[i].startswith('seeds:')):
			getSeeds(input)
			i += 1
		elif(input[i] == 'seed-to-soil map:'):
			i += findtoSoil(i + 1, input)
		elif(input[i] == 'soil-to-fertilizer map:'):
			i += findtoFertilizer(i + 1, input)
		elif(input[i] == 'fertilizer-to-water map:'):
			i += findtoWater(i + 1, input)
		elif(input[i] == 'water-to-light map:'):
			i += findtoLight(i + 1, input)
		elif(input[i] == 'light-to-temperature map:'):
			i += findtoTemperature(i + 1, input)
		elif(input[i] == 'temperature-to-humidity map:'):
			i += findtoHumidity(i + 1, input)
		elif(input[i] == 'humidity-to-location map:'):
			i += findtoLocation(i + 1, input)
		else:
			i += 1


def toSoil(seed):
	for elm in seedtosoil:
		if (seed >= elm[1] and seed < elm[1] + elm[2]):
			return elm[0] + seed - elm[1]
	return seed

def toFertilizer(seed):
	for elm in soiltofertilizer:
		if (seed >= elm[1] and seed < elm[1] + elm[2]):
			return elm[0] + seed - elm[1]
	return seed

def toWater(seed):
	for elm in fertilizertowater:
		if (seed >= elm[1] and seed < elm[1] + elm[2]):
			return elm[0] + seed - elm[1]
	return seed

def toLight(seed):
	for elm in watertolight:
		if (seed >= elm[1] and seed < elm[1] + elm[2]):
			return elm[0] + seed - elm[1]
	return seed

def toTemperature(seed):
	for elm in lighttotemperature:
		if (seed >= elm[1] and seed < elm[1] + elm[2]):
			return elm[0] + seed - elm[1]
	return seed

def toHumidity(seed):
	for elm in temperaturetohumidity:
		if (seed >= elm[1] and seed < elm[1] + elm[2]):
			return elm[0] + seed - elm[1]
	return seed

def toLocation(seed):
	for elm in humiditytolocation:
		if (seed >= elm[1] and seed < elm[1] + elm[2]):
			return elm[0] + seed - elm[1]
	return seed

def part_one():
	result = sys.maxsize
	for seed in seeds:
		seed = toSoil(seed)
		seed = toFertilizer(seed)
		seed = toWater(seed)
		seed = toLight(seed)
		seed = toTemperature(seed)
		seed = toHumidity(seed)
		seed = toLocation(seed)
		if (seed < result):
			result = seed
	print('Part one: ', result)

def part_two():
	#tested some to find the range the result is in with increasing the steps and start
	result = 40000000
	while True:
		seed = result
		for elm in humiditytolocation:
			if (seed >= elm[0] and seed < elm[0] + elm[2]):
				seed = elm[1] + seed - elm[0]
				break
		for elm in temperaturetohumidity:
			if (seed >= elm[0] and seed < elm[0] + elm[2]):
				seed =  elm[1] + seed - elm[0]
				break
		for elm in lighttotemperature:
			if (seed >= elm[0] and seed < elm[0] + elm[2]):
				seed =  elm[1] + seed - elm[0]
				break
		for elm in watertolight:
			if (seed >= elm[0] and seed < elm[0] + elm[2]):
				seed =  elm[1] + seed - elm[0]
				break
		for elm in fertilizertowater:
			if (seed >= elm[0] and seed < elm[0] + elm[2]):
				seed =  elm[1] + seed - elm[0]
				break
		for elm in soiltofertilizer:
			if (seed >= elm[0] and seed < elm[0] + elm[2]):
				seed =  elm[1] + seed - elm[0]
				break
		for elm in seedtosoil:
			if (seed >= elm[0] and seed < elm[0] + elm[2]):
				seed =  elm[1] + seed - elm[0]
				break
		i = 0
		while i < len(seeds) - 1:
			if (seed >= seeds[i] and seed < seeds[i] + seeds[i + 1]):
				print('Part two: ', result)
				return
			i += 2
		result += 1


read_input()
part_one()
part_two()
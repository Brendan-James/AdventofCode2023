import copy
data = """my input""".split("\n")

originaldata = copy.deepcopy(data)

def transpose(array):
	newarray = []
	for i in range(len(array[0])):
		nexus = ""
		for j in range(len(array)):
			nexus+=array[j][i]
		newarray.append(nexus)
	return newarray


newdata = []

for i in data:
	newdata.append(copy.deepcopy(i))
	if not any([x=="#" for x in i]):
		newdata.append(copy.deepcopy(i))

data = transpose(newdata)
newdata = []

for i in data:
	newdata.append(copy.deepcopy(i))
	if not any([x=="#" for x in i]):
		newdata.append(copy.deepcopy(i))

data = transpose(newdata)

galaxies = []
for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x]=="#":
			galaxies.append((x,y))

total = 0
for i in range(len(galaxies)):
	for j in range(i+1,len(galaxies)):
		total+=abs(galaxies[i][0]-galaxies[j][0])
		total+=abs(galaxies[i][1]-galaxies[j][1])

print(total)

crossingpointsX = []
crossingpointsY = []
data = originaldata

for i in range(len(data)):
	if not any([x=="#" for x in data[i]]):
		crossingpointsY.append(i)
for i in range(len(data[0])):
	if not any([x[i]=="#" for x in data]):
		crossingpointsX.append(i)

galaxies = []
for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x]=="#":
			galaxies.append((x,y))

total = 0
for i in range(len(galaxies)):
	for j in range(i+1,len(galaxies)):
		total+=abs(galaxies[i][0]-galaxies[j][0])
		total+=abs(galaxies[i][1]-galaxies[j][1])
		for x in crossingpointsX:
			if galaxies[i][0]<x<galaxies[j][0] or galaxies[j][0]<x<galaxies[i][0]:
				total+= 999999
		for x in crossingpointsY:
			if galaxies[i][1]<x<galaxies[j][1] or galaxies[j][1]<x<galaxies[i][1]:
				total+= 999999

print(total)

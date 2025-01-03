import copy
data = """my input""".split("\n")


for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x] == "S":
			positions = {(x,y):True}

for step in range(64):
	newpositions = {}
	for x,y in positions:
		if not 0<=x<len(data[0]) or not 0<=y<len(data):
			continue
		if data[y][x] == "#":
			continue
		newpositions[(x+1,y)] = True
		newpositions[(x-1,y)] = True
		newpositions[(x,y+1)] = True
		newpositions[(x,y-1)] = True
	positions = newpositions

total = 0
for x,y in positions:
	if not 0<=x<len(data[0]) or not 0<=y<len(data):
		continue
	if data[y][x] == "#":
		continue
	total+=1
print(total)
	
for step in range(100):
	newpositions = {}
	for x,y in positions:
		if not 0<=x<len(data[0]) or not 0<=y<len(data):
			continue
		if data[y][x] == "#":
			continue
		newpositions[(x+1,y)] = True
		newpositions[(x-1,y)] = True
		newpositions[(x,y+1)] = True
		newpositions[(x,y-1)] = True
	positions = newpositions

even = 0
for x,y in positions:
	if not 0<=x<len(data[0]) or not 0<=y<len(data):
		continue
	if data[y][x] == "#":
		continue
	even+=1
print("even",even)

newpositions = {}
for x,y in positions:
	if not 0<=x<len(data[0]) or not 0<=y<len(data):
		continue
	if data[y][x] == "#":
		continue
	newpositions[(x+1,y)] = True
	newpositions[(x-1,y)] = True
	newpositions[(x,y+1)] = True
	newpositions[(x,y-1)] = True
positions = newpositions

odd = 0
for x,y in positions:
	if not 0<=x<len(data[0]) or not 0<=y<len(data):
		continue
	if data[y][x] == "#":
		continue
	odd+=1
print("odd",odd)

for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x] == "S":
			positions = {(x,y):{(0,0):True}}

def assimilate(target,wraps):
	global newpositions
	global done
	if target not in newpositions:
		newpositions[target] = {}
	for i in wraps:
		if i not in done:
			newpositions[target][i] = True

done = {}

total = 0
odds = 0
evens = 0

for step in range(589):
	print(step)
	newpositions = {}
	for x,y in positions:
		assimilate((x+1,y),positions[(x,y)])
		assimilate((x-1,y),positions[(x,y)])
		assimilate((x,y+1),positions[(x,y)])
		assimilate((x,y-1),positions[(x,y)])
	positions = newpositions
	newpositions = {}
	for x,y in positions:
		if not 0<=x<len(data[0]) or not 0<=y<len(data):
			wrappedx = x%len(data[0])
			wrappedy = y%len(data)
			if x<0:
				modifier = (-1,0)
			elif x>=len(data[0]):
				modifier = (1,0)
			elif y<0:
				modifier = (0,1)
			else:
				modifier = (0,-1)
			screens = {}
			for i in positions[(x,y)]:
				screens[(i[0]+modifier[0],i[1]+modifier[1])] = True
			assimilate((wrappedx,wrappedy),screens)
		else:
			if data[y][x] == "#":
				continue
			assimilate((x,y),positions[(x,y)])
	positions = newpositions
	counts = {}
	for i in positions:
		for j in positions[i]:
			if j not in counts:
				counts[j] = 0
			counts[j]+=1
	if step%2==1:
		continue
	for i in counts:
		if (i[0]+i[1])%2==1:
			if counts[i] == even:
				done[i] = True
				total+=even
		else:
			if counts[i] == odd:
				done[i] = True
				total+=odd

counts = {}
for i in positions:
	for j in positions[i]:
		if j not in counts:
			counts[j] = 0
		counts[j]+=1

print(counts)
squareses = 26501365//len(data)
print(squareses)

# it's time for math

truetotal = 0

truetotal+= squareses**2 * even
truetotal+= (squareses-1)**2 * odd
truetotal+= counts[(4,0)]
truetotal+= counts[(-4,0)]
truetotal+= counts[(0,4)]
truetotal+= counts[(0,-4)]
truetotal+= counts[(2,2)]*(squareses-1)
truetotal+= counts[(-2,2)]*(squareses-1)
truetotal+= counts[(2,-2)]*(squareses-1)
truetotal+= counts[(-2,-2)]*(squareses-1)
truetotal+= counts[(2,3)]*squareses
truetotal+= counts[(-2,3)]*squareses
truetotal+= counts[(2,-3)]*squareses
truetotal+= counts[(-2,-3)]*squareses
print(truetotal)

for i in positions:
	total+=len([j not in done for j in positions[i]])
print(total)

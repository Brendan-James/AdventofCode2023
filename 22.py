data = """my input""".split("\n")

data = [[[int(k) for k in j.split(",")] for j in i.split("~")] for i in data]

bricks = []

for i in data:
	brick = []
	for x in range(min(i[0][0],i[1][0]),max(i[0][0],i[1][0])+1):
		for y in range(min(i[0][1],i[1][1]),max(i[0][1],i[1][1])+1):
			for z in range(min(i[0][2],i[1][2]),max(i[0][2],i[1][2])+1):
				brick.append((x,y,z))
	bricks.append(brick)

flag = True

positionslist = {}
for i in bricks:
	for (x,y,z) in i:
		positionslist[(x,y,z)] = True

while flag:
	flag = False
	for i in reversed(bricks):
		below = []
		for x,y,z in i:
			below.append((x,y,z-1))
		for x,y,z in below:
			if z<=0:
				break
			if (x,y,z) in i:
				continue
			if (x,y,z) in positionslist:
				break
		else:
			bricks.remove(i)
			bricks.append(below)
			for x,y,z in i:
				positionslist.pop((x,y,z))
				positionslist[(x,y,z-1)] = True 
			flag = True
			break

supportingcast = {}

for i in range(len(bricks)):
	supporters = {}
	cont = True
	for j in range(len(bricks)):
		if j==i:
			continue
		for x,y,z in bricks[i]:
			if (x,y,z-1) in bricks[j]:
				supporters[j] = True
	supportingcast[i] = supporters

solos = {}
for i in supportingcast:
	if len(supportingcast[i]) == 1:
		for j in supportingcast[i]:
			solos[j] = True

print(len(bricks)-len(solos))

total = 0

for i in range(len(bricks)):
	fallers = [i]
	flag = True
	while flag:
		flag = False
		for j in supportingcast:
			if len(supportingcast[j]) == 0:
				continue
			if j in fallers:
				continue
			if all([k in fallers for k in supportingcast[j]]):
				fallers.append(j)
				flag = True
	total+=len(fallers)-1

print(total)

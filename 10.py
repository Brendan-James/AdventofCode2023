data = """my input""".split("\n")
start = False
directions = {"F":((1,0),(0,1)),"J":((-1,0),(0,-1)),"L":((1,0),(0,-1)),"7":((-1,0),(0,1)),"|":((0,-1),(0,1)),"-":((1,0),(-1,0))}
mods = [(-1,0),(1,0),(0,-1),(0,1)]
for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x]=="S":
			start = (x,y)
			break
	if start:
		break

def check(pos,dirt):
	global data
	global directions
	pos = addvec(pos,dirt)
	if (not 0<=pos[0]<len(data[0])) or (not 0<=pos[1]<len(data)):
		return False
	target = data[pos[1]][pos[0]]
	if target == "." or target=="S":
		return False
	oppo = inv(dirt)
	if oppo in directions[target]:
		return True
	return False
def addvec(a,b):
	return (a[0]+b[0],a[1]+b[1])
def inv(a):
	return (a[0]*-1,a[1]*-1)
def rotate(a):
	return (a[1],a[0]*-1)

locations = []
for x,i in enumerate(mods):
	if check(start,i):
		locations.append((addvec(start,i),inv(i),x))

AAA = locations[0][2]
BBB = locations[1][2]

steps = 0
visits = [start,locations[0][0],locations[1][0]]
checksquaresa = []
checksquaresb = []
while len(locations)!=0:
	steps+=1
	newlocations = []
	for i in locations:
		before = True
		looking = i[1]
		for x in range(3):
			looking = rotate(looking)
			if looking in directions[data[i[0][1]][i[0][0]]]:
				before = False
				continue
			if (i[2]==AAA) ^ before:
				checksquaresa.append(addvec(i[0],looking))
			else:
				checksquaresb.append(addvec(i[0],looking))
		for j in directions[data[i[0][1]][i[0][0]]]:
			if j == i[1]:
				continue
			target = addvec(i[0],j)
			if target not in visits:
				visits.append(target)
				newlocations.append((target,inv(j),i[2]))
	locations = newlocations

print(steps)

VISGRID = [[False for i in range(len(data[0]))] for j in range(len(data))]

def edgefind(pos):
	global visits
	global VISGRID
	global mods
	if (not 0<=pos[0]<len(VISGRID[0])) or (not 0<=pos[1]<len(VISGRID)):
		return True
	if pos in visits or VISGRID[pos[1]][pos[0]]:
		return False
	VISGRID[pos[1]][pos[0]] = True
	for i in mods:
		if edgefind(addvec(pos,i)):
			return True
	return False

flag = True

for i in checksquaresa:
	if edgefind(i):
		break
else:
	flag = False

if flag:
	VISGRID = [[False for i in range(len(data[0]))] for j in range(len(data))]
	for i in checksquaresb:
		edgefind(i)
total = 0

for y in range(len(data)):
	out = ""
	for x in range(len(data[0])):
		if VISGRID[y][x]:
			total+=1
			out+="*"
		elif (x,y) in visits:
			out+= data[y][x]
		else:
			out+="."
	print(out)
print(total)

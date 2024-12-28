import copy
data = """my input""".split("\n")

data = [i.split(" ") for i in data]
data = [[list(i[0]),[int(j) for j in i[1].split(",")]] for i in data]

#rawdata = copy.deepcopy(data)


""" # PART 1 (is slow and also destroys data)

def locate(s):
	locs = []
	for i in range(len(s)):
		if s[i]=="?":
			locs.append(i)
	return locs

def calc(s):
	counts = []
	currently = False
	current = 0
	for i in s:
		if i=="." and currently:
			currently = False
			counts.append(current)
			current = 0
		elif i=="#":
			currently = True
			current+=1
	if currently:
		counts.append(current)
	return counts

def increment(l,pos):
	if l[pos]==".":
		l[pos] = "#"
		return l
	l[pos] = "."
	return increment(l,pos+1)


total = 0
for x,i in enumerate(data):
	print(x,len(data))
	posse = locate(i[0])
	arrangement = ["." for x in range(len(posse))]
	while "." in arrangement:
		for j in range(len(posse)):
			i[0][posse[j]] = arrangement[j]
		#print(x,i[0],calc(i[0]),calc(i[0]) == i[1])
		if calc(i[0]) == i[1]:
			total+=1
		increment(arrangement,0)
	for j in range(len(posse)):
		i[0][posse[j]] = arrangement[j]
	#print(x,i[0],calc(i[0]),calc(i[0]) == i[1])
	if calc(i[0]) == i[1]:
		total+=1
	print(rawdata[x],total)
	total = 0

print(total)
"""

newdata = []

for i in data:
	newi = copy.deepcopy(i)
	for x in range(4):
		newi[0]+="?"
		for j in i[1]:
			newi[1].append(j)
		for j in i[0]:
			newi[0].append(j)
	newdata.append(newi)

data = newdata
total = 0

def search(space,target):
	successes = []
	for i in range(0,len(space)-target+1):
		if i!=0:
			if space[i-1] == "#":
				continue
		if i+target!=len(space):
			if space[i+target] == "#":
				continue
		if "." in space[i:i+target]:
			continue
		successes.append(i)
	return successes

def crunch(targets,mini):
	global vals
	global required
	total = 0
	if len(targets) == 0:
		if len(required)==0:
			return sum(mini.values())
		for i in mini:
			if i>required[-1]:
				total+=mini[i]
		return total
	newmini = {}
	for i in vals[targets[0]]:
		for j in mini:
			if i<j:
				continue
			for x in required:
				if j<=x<i:
					break
			else:
				if i+targets[0]+1 not in newmini:
					newmini[i+targets[0]+1] = 0
				newmini[i+targets[0]+1] += mini[j]
	return crunch(targets[1:],newmini)

for x,i in enumerate(data):
	vals = {}
	for j in list(set(i[1])):
		vals[j] = search(i[0],j)
	required = []
	for j in range(len(i[0])):
		if i[0][j] == "#":
			required.append(j)
	total+=crunch(i[1],{0:1})

print(total)

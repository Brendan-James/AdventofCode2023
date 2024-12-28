import copy
# I replaced all instances of \ with < to prevent excess escaped characters
data = """my input with the caveat in the above comment""".split("\n")

visited = [[False for i in range(len(data[0]))] for j in range(len(data))]

beams = [[0,0,"right"]]
directions = {"up":(0,-1),"down":(0,1),"left":(-1,0),"right":(1,0)}

before = []

flag = True
while flag:
	flag = False
	newbeams = []
	for x in beams:
		if x in before:
			continue
		else:
			before.append(x)
			flag = True
		i = copy.deepcopy(x)
		if (not 0<=i[0]<len(data[0])) or (not 0<=i[1]<len(data)):
			continue
		if not visited[i[0]][i[1]]:
			visited[i[0]][i[1]] = True
		target = data[i[1]][i[0]]
		if target == "." or (target=="-" and (i[2]=="left" or i[2]=="right")) or (target=="|" and (i[2]=="up" or i[2]=="down")):
			i[0]+=directions[i[2]][0]
			i[1]+=directions[i[2]][1]
			newbeams.append([i[0],i[1],i[2]])
		elif target == "/":
			if i[2] == "up":
				i[2] = "right"
			elif i[2] == "right":
				i[2] = "up"
			elif i[2] == "down":
				i[2] = "left"
			else:
				i[2] = "down"
			i[0]+=directions[i[2]][0]
			i[1]+=directions[i[2]][1]
			newbeams.append([i[0],i[1],i[2]])
		elif target == "<":
			if i[2] == "up":
				i[2] = "left"
			elif i[2] == "left":
				i[2] = "up"
			elif i[2] == "down":
				i[2] = "right"
			else:
				i[2] = "down"
			i[0]+=directions[i[2]][0]
			i[1]+=directions[i[2]][1]
			newbeams.append([i[0],i[1],i[2]])
		elif target == "-":
			j = copy.deepcopy(i)
			i[2] = "left"
			j[2] = "right"
			i[0]+=directions[i[2]][0]
			i[1]+=directions[i[2]][1]
			newbeams.append([i[0],i[1],i[2]])
			j[0]+=directions[j[2]][0]
			j[1]+=directions[j[2]][1]
			newbeams.append([j[0],j[1],j[2]])
		elif target == "|":
			j = copy.deepcopy(i)
			i[2] = "up"
			j[2] = "down"
			i[0]+=directions[i[2]][0]
			i[1]+=directions[i[2]][1]
			newbeams.append([i[0],i[1],i[2]])
			j[0]+=directions[j[2]][0]
			j[1]+=directions[j[2]][1]
			newbeams.append([j[0],j[1],j[2]])
	beams = newbeams

print(sum([sum(i) for i in visited]))

entrances = []
for i in range(len(data)):
	entrances.append([0,i,"right"])
	entrances.append([len(data[0])-1,i,"left"])
	entrances.append([i,0,"down"])
	entrances.append([i,len(data)-1,"up"])

best = 0

for n,start in enumerate(entrances):
	print(n,len(entrances))
	visited = [[False for i in range(len(data[0]))] for j in range(len(data))]

	beams = [start]
	directions = {"up":(0,-1),"down":(0,1),"left":(-1,0),"right":(1,0)}

	before = []

	flag = True
	while flag:
		flag = False
		newbeams = []
		for x in beams:
			if x in before:
				continue
			else:
				before.append(x)
				flag = True
			i = copy.deepcopy(x)
			if (not 0<=i[0]<len(data[0])) or (not 0<=i[1]<len(data)):
				continue
			if not visited[i[0]][i[1]]:
				visited[i[0]][i[1]] = True
			target = data[i[1]][i[0]]
			if target == "." or (target=="-" and (i[2]=="left" or i[2]=="right")) or (target=="|" and (i[2]=="up" or i[2]=="down")):
				i[0]+=directions[i[2]][0]
				i[1]+=directions[i[2]][1]
				newbeams.append([i[0],i[1],i[2]])
			elif target == "/":
				if i[2] == "up":
					i[2] = "right"
				elif i[2] == "right":
					i[2] = "up"
				elif i[2] == "down":
					i[2] = "left"
				else:
					i[2] = "down"
				i[0]+=directions[i[2]][0]
				i[1]+=directions[i[2]][1]
				newbeams.append([i[0],i[1],i[2]])
			elif target == "<":
				if i[2] == "up":
					i[2] = "left"
				elif i[2] == "left":
					i[2] = "up"
				elif i[2] == "down":
					i[2] = "right"
				else:
					i[2] = "down"
				i[0]+=directions[i[2]][0]
				i[1]+=directions[i[2]][1]
				newbeams.append([i[0],i[1],i[2]])
			elif target == "-":
				j = copy.deepcopy(i)
				i[2] = "left"
				j[2] = "right"
				i[0]+=directions[i[2]][0]
				i[1]+=directions[i[2]][1]
				newbeams.append([i[0],i[1],i[2]])
				j[0]+=directions[j[2]][0]
				j[1]+=directions[j[2]][1]
				newbeams.append([j[0],j[1],j[2]])
			elif target == "|":
				j = copy.deepcopy(i)
				i[2] = "up"
				j[2] = "down"
				i[0]+=directions[i[2]][0]
				i[1]+=directions[i[2]][1]
				newbeams.append([i[0],i[1],i[2]])
				j[0]+=directions[j[2]][0]
				j[1]+=directions[j[2]][1]
				newbeams.append([j[0],j[1],j[2]])
		beams = newbeams

	best = max(best,sum([sum(i) for i in visited]))

print(best)

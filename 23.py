import copy
data = """my input""".split("\n")

nexus = []
directions = {"r":(1,0),"l":(-1,0),"d":(0,1),"u":(0,-1)}
opposite = {"r":"l","l":"r","u":"d","d":"u"}
arrows = {"v":"d",">":"r","<":"l","^":"u"}

for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x]!=".":
			continue
		validdirs = 0
		for i in directions.values():
			newx = x+i[0]
			newy = y+i[1]
			if not (0<=newx<len(data[0]) and 0<=newy<len(data)):
				continue
			if data[newy][newx] != "#":
				validdirs+=1
		if validdirs!=2:
			nexus.append((x,y))

pathways = {}

for x,y in nexus:
	steps = 0
	todo = [(x+1,y,"r","="),(x-1,y,"l","="),(x,y+1,"d","="),(x,y-1,"u","=")]
	while len(todo)>0:
		steps+=1
		newtodo = []
		for newx,newy,prevdir,polarity in todo:
			if not (0<=newx<len(data[0]) and 0<=newy<len(data)):
				continue
			if data[newy][newx] == "#":
				continue
			if (newx,newy) in nexus:
				a = nexus.index((x,y))
				b = nexus.index((newx,newy))
				if b<a:
					if polarity == "<":
						polarity = ">"
					else:
						polarity = "<"
				pathways[(min(a,b),max(a,b))] = (steps,polarity)
				continue
			if data[newy][newx] in arrows:
				if prevdir == arrows[data[newy][newx]]:
					polarity = ">"
				else:
					polarity = "<"
			for i in directions:
				if i == opposite[prevdir]:
					continue
				newtodo.append((newx+directions[i][0],newy+directions[i][1],i,polarity))
		todo = newtodo

ultimate = len(nexus)-1
for i in pathways:
	if i[0] == ultimate:
		penultimate = i[1]
		extra = pathways[i][0]
	if i[1] == ultimate:
		penultimate = i[0]
		extra = pathways[i][0]

positions = [(0,0,{})]
results = []

while len(positions)>0:
	newpositions = []
	for current,distance,visited in positions:
		visited[current] = True
		if current == ultimate:
			results.append(distance)
			continue
		for path in pathways:
			if current == path[0] and pathways[path][1] == ">":
				if path[1] in visited:
					continue
				newpositions.append((path[1],distance+pathways[path][0],copy.deepcopy(visited)))
			elif current == path[1] and pathways[path][1] == "<":
				if path[0] in visited:
					continue
				newpositions.append((path[0],distance+pathways[path][0],copy.deepcopy(visited)))
	positions = newpositions
print(max(results))

best = 0

edges = ""

for i in pathways:
	if pathways[i][1] == ">":
		edges+=str(i[0])+"->"+str(i[1])+","
	else:
		edges+=str(i[1])+"->"+str(i[0])+","

print(edges[:-1])

# this code doesn't actually halt in a reasonable amount of time so I just kinda guess when I think it has the best answer and submit that
# the best answer is 6726 btw
def undirdelve(node,distance,visited):
	global pathways
	global penultimate
	global extra
	global best
	if node == penultimate:
		if distance+extra>best:
			best = distance+extra
			print(best)
		return distance+extra
	if node in visited:
		return 0
	visited[node] = True
	results = []
	nexts = []
	for path in pathways:
		if path[0] == node:
			nexts.append((pathways[path][0],path[1]))
		if path[1] == node:
			nexts.append((pathways[path][0],path[0]))
	nexts = sorted(nexts)
	for i in reversed(nexts):
		results.append(undirdelve(i[1],distance+i[0],copy.deepcopy(visited)))
	return max(results)

print(undirdelve(0,0,{}))

import copy
rules = """my input pt 1""".split("\n")

objects = """my input pt 2""".split("\n")

newobs = []
for i in objects:
	newobs.append(i[1:-1].split(","))

objects = []
for i in newobs:
	current = {}
	for j in i:
		current[j[0]] = int(j[2:])
	objects.append(current)

newrules = []

for i in rules:
	newrules.append(i[:-1].split("{"))

rules = {}

for name, contents in newrules:
	newcontents = []
	for i in contents.split(","):
		if ":" not in i:
			newcontents.append((("x","TRUE",1),i))
			break
		decider, result = i.split(":")
		if ">" in decider:
			letter,number = decider.split(">")
			newcontents.append(((letter,">",int(number)),result))
		else:
			letter,number = decider.split("<")
			newcontents.append(((letter,"<",int(number)),result))
	rules[name] = newcontents

def evaluate(obj,rule):
	global rules
	relevant = rules[rule]
	for i in relevant:
		if i[0][1] == "TRUE":
			return deepen(obj,i[1])
		if i[0][1] == "<":
			if obj[i[0][0]]<i[0][2]:
				return deepen(obj,i[1])
		elif obj[i[0][0]]>i[0][2]:
			return deepen(obj,i[1])

def deepen(obj,result):
	if result == "R":
		return False
	if result == "A":
		return True
	return evaluate(obj,result)

total = 0
for i in objects:
	if evaluate(i,"in"):
		for j in i:
			total+=i[j]

print(total)

ranges = [("in",{"x":[1,4000],"m":[1,4000],"a":[1,4000],"s":[1,4000]})]
total = 0

def resolve(c,result):
	global ranges
	global total
	if result == "R":
		return
	if result == "A":
		additional = 1
		for i in c:
			additional*=c[i][1]-c[i][0]+1
		total+=additional
		return
	ranges.append((result,c))

while len(ranges) > 0:
	rule, c = ranges.pop(0)
	for decider, result in rules[rule]:
		if decider[1] == "TRUE":
			 resolve(c,result)
		elif decider[1] == "<":
			if c[decider[0]][0]>=decider[2]:
				continue
			new = copy.deepcopy(c)
			new[decider[0]][1] = decider[2]-1
			resolve(new,result)
			c[decider[0]][0] = decider[2]
		else:
			if c[decider[0]][1]<=decider[2]:
				continue
			new = copy.deepcopy(c)
			new[decider[0]][0] = decider[2]+1
			resolve(new,result)
			c[decider[0]][1] = decider[2]

print(total)

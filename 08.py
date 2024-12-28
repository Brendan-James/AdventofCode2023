import numpy
sequence = "my input pt 1"

data = """my input pt 2""".split("\n")

nodes = {}
for i in data:
	nodes[i[0:3]] = [i[7:10],i[12:15]]

location = "AAA"
steps = 0
while location!="ZZZ":
	for l in sequence:
		if l == "L":
			location = nodes[location][0]
		else:
			location = nodes[location][1]
		steps+=1
		if location=="ZZZ":
			break
print(steps)


locations = []
for i in nodes:
	if i[-1]=="A":
		locations.append(i)



steps = 0
loops = []
for i in locations:
	location = i
	trail = []
	flag = True
	while flag:
		for j,l in enumerate(sequence):
			if str(j)+location in trail:
				flag = False
				break
			trail.append(str(j)+location)
			if l == "L":
				location = nodes[location][0]
			else:
				location = nodes[location][1]
	loops.append([trail[trail.index(str(j)+location):],trail.index(str(j)+location)])

for i in loops:
	for j,v in enumerate(i[0]):
		i[0][j] = v[-1]=="Z"

n = []
a = []
for i in loops:
	n.append(len(i[0]))
	a.append((i[0].index(True)+i[1])%n[-1])


print(n)
print(a)
# n == a apparently
total = 1
for i in n:
	total = numpy.lcm(total,i)

print(total)
#print(steps)

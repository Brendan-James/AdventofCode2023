import math

data = """my input""".split("\n")

data = [i.split(" -> ") for i in data]
newdata = {}
for i in data:
	newdata[i[0][1:]] = (i[0][0],i[1].split(", "))
data = newdata

states = {}

for i in data:
	if data[i][0] == "b":
		continue
	if data[i][0] == "%":
		states[i] = False
	else:
		ands = {}
		for j in data:
			for k in data[j][1]:
				if k == i:
					ands[j] = False
		states[i] = ands

highs = 0
lows = 0
todo = []

def pulse(height,target,previous):
	global data
	global states
	global highs
	global lows
	global todo
	if height:
		highs+=1
	else:
		lows+=1
	if target not in data:
		return
	if data[target][0] == "b" :
		for i in data[target][1]:
			todo.append((height,i,target))
		return
	if data[target][0] == "%":
		if not height:
			states[target] = not states[target]
			for i in data[target][1]:
				todo.append((states[target],i,target))
		return
	states[target][previous] = height
	for i in data[target][1]:
		todo.append((not all(states[target].values()),i,target))

for x in range(1000):
	pulse(False,"roadcaster","button")
	while len(todo)>0:
		a,b,c = todo.pop(0)
		pulse(a,b,c)

print(highs*lows)

# it's time for logic

# nevermind, apparently my logic is for naught



def find(value):
	global data
	results = []
	for i in data:
		if value in data[i][1]:
			results.append(i)
	return results
"""
def delve(target):
	global data
	priors = find(target)
	result = []
	for i in priors:
		if data[i][0]=="%":
			fun = delve(i)
			if len(fun) == 1:
				result.append([fun[0][0],fun[0][1]*2])
			else:
				result.append([fun,2])
		else:
			result.append([i,1])
	return result

logic = {}

for i in data:
	if data[i][0] != "&":
		continue
	logic[i] = delve(i)

logic["rx"] = delve("rx")

newlogic = {}

print(logic["lr"][0])
"""

states = {}

for i in data:
	if data[i][0] == "b":
		continue
	if data[i][0] == "%":
		states[i] = False
	else:
		ands = {}
		for j in data:
			for k in data[j][1]:
				if k == i:
					ands[j] = False
		states[i] = ands

special = find(find("rx")[0])
done = []

def pulse2(height,target,previous):
	global data
	global states
	global todo
	global x
	global special
	global done
	#print(previous,height,target)
	if target not in data:
		return
	if previous in special and height:
		print(previous,x)
		done.append(x)
		special.remove(previous)
	if data[target][0] == "b" :
		for i in data[target][1]:
			todo.append((height,i,target))
		return
	if data[target][0] == "%":
		if not height:
			states[target] = not states[target]
			for i in data[target][1]:
				todo.append((states[target],i,target))
		return
	states[target][previous] = height
	for i in data[target][1]:
		todo.append((not all(states[target].values()),i,target))

todo = []
x = 0
while len(special)>0:
	x+=1
	pulse2(False,"roadcaster","button")
	while len(todo)>0:
		a,b,c = todo.pop(0)
		pulse2(a,b,c)

total = 1
for i in done:
	total = math.lcm(total,i)
print(total)

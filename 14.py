import copy
data = """my input""".split("\n")

data = [list(i) for i in data]

def up(data):
	flag = True

	while flag:
		flag = False
		for y in range(1,len(data)):
			for x in range(len(data[0])):
				if data[y][x] == "O" and data[y-1][x] == ".":
					data[y-1][x] = "O"
					data[y][x] = "."
					flag = True
	return data

data = up(data)

total = 0
for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x]=="O":
			total+=len(data)-y

print(total)

def leftdownright(data):
	flag = True

	while flag:
		flag = False
		for y in range(len(data)):
			for x in range(1,len(data[0])):
				if data[y][x] == "O" and data[y][x-1] == ".":
					data[y][x-1] = "O"
					data[y][x] = "."
					flag = True
	flag = True

	while flag:
		flag = False
		for y in range(len(data)-1):
			for x in range(len(data[0])):
				if data[y][x] == "O" and data[y+1][x] == ".":
					data[y+1][x] = "O"
					data[y][x] = "."
					flag = True
	flag = True

	while flag:
		flag = False
		for y in range(len(data)):
			for x in range(len(data[0])-1):
				if data[y][x] == "O" and data[y][x+1] == ".":
					data[y][x+1] = "O"
					data[y][x] = "."
					flag = True
	return data
	
previous = []
data = leftdownright(data)
cycles = 1
while data not in previous:
	previous.append(copy.deepcopy(data))
	data = leftdownright(up(data))
	cycles+=1

loopstart = previous.index(data)

loop = previous[loopstart:]
position = (1000000000-loopstart-1)%len(loop)
data = loop[position]

total = 0
for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x]=="O":
			total+=len(data)-y

print(total)

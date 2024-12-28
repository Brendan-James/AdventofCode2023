data = "my input".split(",")

def HASH(s):
	x = 0
	for i in s:
		x+=ord(i)
		x*=17
		x=x%256
	return x

total = 0
for i in data:
	total+=HASH(i)

print(total)

boxes = [[] for i in range(256)]

for i,v in enumerate(data):
	if "-" in v:
		data[i] = [v[:-1],False,0]
	else:
		data[i] = [v[:-2],True,v[-1]]

for i in data:
	box = HASH(i[0])
	if i[1]:
		for j in boxes[box]:
			if j[0] == i[0]:
				j[1] = i[2]
				break
		else:
			boxes[box].append([i[0],i[2]])
	else:
		replacement = []
		for j in boxes[box]:
			if j[0]!=i[0]:
				replacement.append(j)
		boxes[box] = replacement

total = 0
for x,box in enumerate(boxes):
	for i,v in enumerate(box):
		total+=int(v[1])*(i+1)*(x+1)


print(total)

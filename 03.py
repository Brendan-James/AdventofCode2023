data = """my input""".split("\n")

data2 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n")

for i,v in enumerate(data):
	data[i]=list(v)

digits = "0123456789"
validation = [["." for i in range(len(data[0]))] for j in range(len(data))]

def numfill(x,y,data,grid):
	digits = "0123456789"
	if data[y][x] not in digits:
		return
	if x==0 or data[y][x-1] not in digits:
		grid[y][x] = "H"
		return

	else:
		return numfill(x-1,y,data,grid)

def numread(x,y,data,prior):
	digits = "0123456789"
	if x==len(data[0])-1 or data[y][x+1] not in digits:
		data[y][x] = prior * 10 + int(data[y][x])
		return data[y][x]
	else:
		data[y][x] = numread(x+1,y,data,prior*10+int(data[y][x]))
		return data[y][x]



for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x] not in digits and data[y][x] != ".":
			for moddedy in [y-1,y,y+1]:
				if moddedy<0 or moddedy>=len(data):
					continue
				for moddedx in [x-1,x,x+1]:
					if moddedx<0 or moddedx>=len(data[0]):
						continue
					numfill(moddedx,moddedy,data,validation)

total = 0
for y in range(len(data)):
	for x in range(len(data[0])):
		if validation[y][x] == "H":
			total+=numread(x,y,data,0)

print(total)

total = 0
for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x] == "*":
			dicty = {}
			for moddedy in [y-1,y,y+1]:
				if moddedy<0 or moddedy>=len(data):
					continue
				for moddedx in [x-1,x,x+1]:
					if moddedx<0 or moddedx>=len(data[0]):
						continue
					if type(data[moddedy][moddedx])==int:
						dicty[data[moddedy][moddedx]] = True
			if len(dicty.keys())==2:
				added = 1
				for i in dicty.keys():
					added*=i
				total+=added
print(total)

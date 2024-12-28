data = """my input""".split("\n")

data = [[int(i) for i in j.split(" ")] for j in data]

total = 0
total2 = 0
for i in data:
	current = [i]
	flag = True
	while flag:
		for j in current[-1]:
			if j!=0:
				nextup = []
				for k in range(len(current[-1])-1):
					nextup.append(current[-1][k+1]-current[-1][k])
				current.append(nextup)
				break
		else:
			temp = 0
			for j in reversed(current):
				total+=j[-1]
				temp = j[0]-temp
			total2+=temp
			flag = False
			break

print(total)
print(total2)

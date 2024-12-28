data = """my input""".replace("  ", " ").split("\n")

data = [i[i.find(":")+2:] for i in data]
data = [i.split(" | ") for i in data]
data = [[j.split(" ") for j in i] for i in data]

total = 0

def score(card):
	total = 0
	for j in card[0]:
		if j in card[1]:
			total+=1
	return total

for i in data:
	total+=math.floor(2**((score(i))-1))

print(total)

counts = [0]*len(data)

for i in reversed(range(len(data))):
	total = 1
	for j in range(score(data[i])+1):
		total+=counts[i+j]
	counts[i] = total

print(sum(counts))

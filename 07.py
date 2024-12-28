from functools import cmp_to_key
import copy
data = """my input""".split("\n")

data = [[list(i.split(" ")[0]),int(i.split(" ")[1]),0] for i in data]
data2 = copy.deepcopy(data)

convert = {"T":10,"J":11,"Q":12,"K":13,"A":14}

for i in data:
	for j in range(5):
		if i[0][j] in convert:
			i[0][j] = convert[i[0][j]]
		else:
			i[0][j] = int(i[0][j])

for i in data:
	sete = {}
	for j in i[0]:
		if j not in sete:
			sete[j] = 1
		else:
			sete[j]+= 1
	groups = {1:0,2:0,3:0,4:0,5:0}
	for j in sete:
		groups[sete[j]]+= 1
	if groups[2]==1:
		i[2] = 1
	if groups[2]==2:
		i[2] = 2
	if groups[3]==1:
		i[2] = 3
		if groups[2]==1:
			i[2] = 4
	if groups[4]==1:
		i[2] = 5
	if groups[5]==1:
		i[2] = 6

def compare(a,b):
	if a[2]>b[2]:
		return 1
	if b[2]>a[2]:
		return -1
	for i in range(5):
		if a[0][i]>b[0][i]:
			return 1
		if b[0][i]>a[0][i]:
			return -1
	return 0

data = sorted(data,key=cmp_to_key(compare))


total = 0
for i,v in enumerate(data):
	total+=v[1]*(i+1)
print(total)

data = data2

convert = {"T":10,"J":1,"Q":12,"K":13,"A":14}

for i in data:
	for j in range(5):
		if i[0][j] in convert:
			i[0][j] = convert[i[0][j]]
		else:
			i[0][j] = int(i[0][j])

for i in data:
	sete = {}
	jokers = 0
	for j in i[0]:
		if j == 1:
			jokers+=1
			continue
		if j not in sete:
			sete[j] = 1
		else:
			sete[j]+= 1
	if jokers == 5:
		i[2] = 6
		continue
	best = 0
	bestie = ""
	for j in sete:
		if sete[j]>best:
			best = sete[j]
			bestie = j
	sete[bestie]+=jokers
	groups = {1:0,2:0,3:0,4:0,5:0}
	for j in sete:
		groups[sete[j]]+= 1
	if groups[2]==1:
		i[2] = 1
	if groups[2]==2:
		i[2] = 2
	if groups[3]==1:
		i[2] = 3
		if groups[2]==1:
			i[2] = 4
	if groups[4]==1:
		i[2] = 5
	if groups[5]==1:
		i[2] = 6


data = sorted(data,key=cmp_to_key(compare))


total = 0
for i,v in enumerate(data):
	total+=v[1]*(i+1)
print(total)

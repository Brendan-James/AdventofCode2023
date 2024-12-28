indie = """my input""".replace(" ","").replace("red","R").replace("green","G").replace("blue","B").split("\n")


games = [i[i.find(":")+1:] for i in indie]
games = [i.split(";") for i in games]
games = [[j.split(",") for j in i] for i in games]

for x,i in enumerate(games):
	for y,j in enumerate(i):
		final = [0,0,0]
		for k in j:
			if k[-1]=="R":
				final[0]=int(k[:-1])
			if k[-1]=="G":
				final[1]=int(k[:-1])
			if k[-1]=="B":
				final[2]=int(k[:-1])
		games[x][y] = final

total = 0
for i,v in enumerate(games):
	for j in v:
		if j[0]>12:
			break
		if j[1]>13:
			break
		if j[2]>14:
			break
	else:
		total+=i+1
print(total)


total = 0
for i in games:
	bests = [0,0,0]
	for j in i:
		if j[0]>bests[0]:
			bests[0]=j[0]
		if j[1]>bests[1]:
			bests[1]=j[1]
		if j[2]>bests[2]:
			bests[2]=j[2]
	total+=bests[0]*bests[1]*bests[2]
print(total)

import math

seeds = "my input pt 1".split(" ")
data = """my input pt 2""".split("\n\nmap:\n")

data = [[[int(k) for k in j.split(" ")] for j in i.split("\n")] for i in data]
current = [int(i) for i in seeds]

for i in data:
	nexts = []
	for j in i:
		newcurrent = []
		for k in current:
			if j[1]<=k<j[1]+j[2]:
				nexts.append(k+j[0]-j[1])
			else:
				newcurrent.append(k)
		current = newcurrent

	current = nexts+current

print(min(current))

current = []
for i in range(len(seeds)//2):
	current.append([int(seeds[i*2]),int(seeds[i*2])+int(seeds[i*2+1])-1])

for i in data:
	nexts = []
	for j in i:
		newcurrent = []
		lower = j[1]
		upper = j[1]+j[2]-1
		for k in current:
			if k[0]<=upper and k[1]>=lower:
				if k[1]>upper:
					newcurrent.append([upper+1,k[1]])
				if k[0]<lower:
					newcurrent.append([k[0],lower-1])
				nexts.append([max(k[0],lower)-j[1]+j[0],min(k[1],upper)-j[1]+j[0]])
			else:
				newcurrent.append(k)
		current = newcurrent

	current = nexts+current

final = []
for i in current:
	final.append(i[0])

print(min(final))

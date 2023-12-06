Time=[56,71,79,99]
Distance = [334,1135,1350,2430]

total = 1
for i in range(4):
	count = 0
	for v in range(Time[i]):
		d = v*(Time[i]-v)
		if d>Distance[i]:
			count+=1
	total*=count

print(total)

Time=56717999
Distance = 334113513502430
total = 0
for v in range(Time):
	if v*(Time-v)>Distance:
		total+=1
print(total)
# that just works I guess

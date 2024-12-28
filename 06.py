Time=["my input hand processed"]
Distance = ["my input hand processed"]

total = 1
for i in range(4):
	count = 0
	for v in range(Time[i]):
		d = v*(Time[i]-v)
		if d>Distance[i]:
			count+=1
	total*=count

print(total)

Time="my input hand concatenated"
Distance = "my input hand concatenated"
total = 0
for v in range(Time):
	if v*(Time-v)>Distance:
		total+=1
print(total)
# that just works I guess

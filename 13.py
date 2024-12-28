import copy
data = """my input""".split("\n\n")

data = [[list(i) for i in j.split("\n")] for j in data]

def transpose(array): # it's back!
	newarray = []
	for i in range(len(array[0])):
		nexus = ""
		for j in range(len(array)):
			nexus+=array[j][i]
		newarray.append(nexus)
	return newarray

def check(array,mid):
	for i in range(len(array)):
		front = mid-i
		back = mid+i+1
		if front<0 or back>=len(array):
			return True
		if array[front]!=array[back]:
			return False
	return True

total = 0

remember = []

for x,i in enumerate(data):
	for mid in range(len(i)-1):
		if check(i,mid):
			total+=(mid+1)*100
			remember.append((mid,"row"))
	t = transpose(i)
	for mid in range(len(t)-1):
		if check(t,mid):
			total+=mid+1
			remember.append((mid,"col"))

print(total)
total = 0

for x,temp in enumerate(data):
	for a in range(len(temp)):
		for b in range(len(temp[0])):
			i = copy.deepcopy(temp)
			if i[a][b] == ".":
				i[a][b] = "#"
			else:
				i[a][b] = "."
			for mid in range(len(i)-1):
				if remember[x] == (mid,"row"):
					continue
				if check(i,mid):
					total+=(mid+1)*100
			t = transpose(i)
			for mid in range(len(t)-1):
				if remember[x] == (mid,"col"):
					continue
				if check(t,mid):
					total+=mid+1

print(total//2)

indie = """my input""".split("\n")

digits = ["0","1","2","3","4","5","6","7","8","9"]
total = 0
for i in indie:
	first = -1
	last = 0
	for j,v in enumerate(i):
		if v in digits:
			if first == -1:
				first = j
			last = j
	total+=int(i[first]+i[last])

print(total)

total = 0
for i in indie:
	first = -1
	last = 0
	i = i.replace("zero","0ero")
	i = i.replace("one","o1e")
	i = i.replace("two","t2o")
	i = i.replace("three","thr3e")
	i = i.replace("four","4our")
	i = i.replace("five","5ive")
	i = i.replace("six","si6")
	i = i.replace("seven","se7en")
	i = i.replace("eight","ei8ht")
	i = i.replace("nine","n9ne")

	for j,v in enumerate(i):
		if v in digits:
			if first == -1:
				first = j
			last = j
	total+=int(i[first]+i[last])

print(total)

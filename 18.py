data = """my input""".split("\n")

data = [i.split(" ") for i in data]
data = [[i[0],int(i[1]),i[2][2:-1]] for i in data]

filled = {(0,0):"000000"}
current = (0,0)

directions = {"L":(-1,0),"R":(1,0),"U":(0,-1),"D":(0,1)}

for i in data:
	for j in range(i[1]):
		current = (current[0]+directions[i[0]][0],current[1]+directions[i[0]][1])
		filled[current] = i[2]

minx = 0
miny = 0
maxx = 0
maxy = 0

for i in filled:
	minx = min(minx,i[0])
	miny = min(miny,i[1])
	maxx = max(maxx,i[0])
	maxy = max(maxy,i[1])

newfill = {}

for i in filled:
	newfill[(i[0]-minx,i[1]-miny)] = filled[i]

table = [["." for x in range(minx,maxx+1)] for y in range(miny,maxy+1)]

for i in newfill:
	table[i[1]][i[0]] = "#"

def floodfill(x,y):
	global table
	todo = [(x,y)]
	while(len(todo)>0):
		x,y = todo.pop(0)
		if (not 0<=x<len(table[0])) or (not 0<=y<len(table)):
			continue
		if table[y][x] == "#" or table[y][x] == "*":
			continue
		table[y][x] = "*"
		todo.append((x-1,y))
		todo.append((x,y-1))
		todo.append((x+1,y))
		todo.append((x,y+1))

floodfill(0,0)
floodfill(len(table[0])-1,0)
floodfill(0,len(table)-1)
floodfill(len(table[0])-1,len(table)-1)

total = len(table)*len(table[0])

for row in table:
	for cha in row:
		if cha == "*":
			total-=1 

print(total)

newinsts = []
look = "RDLU"

for i in data:
	newinsts.append((int(i[2][:-1],16),look[int(i[2][-1])]))

verticies = []
current = (0,0)
bonus = 0
for i in newinsts:
	current = (current[0]+directions[i[1]][0]*i[0],current[1]+directions[i[1]][1]*i[0])
	verticies.append(current)
	bonus+=i[0]

# gonna be honest, I stole this code from stack exchange
# https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon

def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])

print(int(area(verticies))+bonus//2+1)

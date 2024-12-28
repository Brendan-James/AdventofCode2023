import heapq
data = """my input""".split("\n")

data = [[int(i) for i in list(j)] for j in data]
data[0][0] = 0

directions = {"up":(0,-1),"down":(0,1),"left":(-1,0),"right":(1,0)}
reverse = {"up":"down","down":"up","left":"right","right":"left"}

positions = [(0,0,0,0,"noop",0)]
visited = {}

while len(positions)>0:
	value,x,y,score,prevdir,consec = heapq.heappop(positions)
	if (not 0<=x<len(data[0])) or (not 0<=y<len(data)):
		continue
	if f"{x}-{y}{prevdir}{consec}" in visited:
		continue
	score+=data[y][x]
	if x==len(data[0])-1 and y == len(data)-1:
		print(score)
		break
	visited[f"{x}-{y}{prevdir}{consec}"] = True
	for i in directions:
		if i==prevdir and consec == 3:
			continue
		if prevdir == reverse[i]:
			continue
		newx = x+directions[i][0]
		newy = y+directions[i][1]
		newsteps = 1
		if i == prevdir:
			newsteps += consec
		heapq.heappush(positions,((score-newx)-newy,newx,newy,score,i,newsteps))

positions = [(0,0,0,0,"noop",0)]
visited = {}

while len(positions)>0:
	value,x,y,score,prevdir,consec = heapq.heappop(positions)
	if (not 0<=x<len(data[0])) or (not 0<=y<len(data)):
		continue
	if f"{x}-{y}{prevdir}{consec}" in visited:
		continue
	score+=data[y][x]
	if x==len(data[0])-1 and y == len(data)-1:
		print(score)
		break
	visited[f"{x}-{y}{prevdir}{consec}"] = True
	for i in directions:
		if i==prevdir and consec == 10:
			continue
		if prevdir in directions and consec<4 and i!=prevdir:
			continue
		if prevdir == reverse[i]:
			continue
		newx = x+directions[i][0]
		newy = y+directions[i][1]
		newsteps = 1
		if i == prevdir:
			newsteps += consec
		heapq.heappush(positions,((score-newx)-newy,newx,newy,score,i,newsteps))

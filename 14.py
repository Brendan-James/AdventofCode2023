import copy
data = """..O....O....O..#O#OOOO...O..O...#.O.#.OO...O.##O#.#..#...OOO.#....O#....#...OO..O.OO..#.OOO.O..O.O.O
.OO.##....#.#..#O...........##O..#..O..O.....#.O.##.O.O............#......##........#.OO..#OO..#....
##........O.O.#O...##.#...#.#.O...#..#O...#....#O...OOOO..OO.OOO.O...O.#........OO.O.O....O...O##O..
...O..O#..O.O..O.O..OO..#.....O..OO....O#..O.##..O..#O.#.OO....####.OOO.OO..O.#..OO.O....O...#.#.O..
...#.O.OOO..#O...O#...O....O...#.O.OO.O.O...O...#...#.#O...#....#....#..O....#..O..#...#..O.....O...
.OO...#...#O#....O.O#.O#.O#.OO.OO.O.O#..........O#....O........O.O.....#...O.#....#........#........
.#.#.#.OOO....#.O.#....#.#..##O.........O.#OO.OO..OO#.#....##.#.##O#.#....O.#.........#...O.#O.O....
..O.#.#.O.....O....O.#..#..O#.#OO..OO........#O.#OO.O..OO.O.......#...#.#..##...........O...#.O.#.#.
...#....#...O....##O......O...#...#....O.#...OOO#..#..O....##.OO.......#O.#.....OO....#.###O#O#.....
O..#O..O..OO.OO.O........O.##O.O...O.O##O..#....#.#..O.OO.#.....O.#......O..O#..#.O.#O.#...#O....O..
OO...O.......#........O#.#.....#O.O...O.O........O.##O......OO.....#.....O#...O#.#..#...#.#O..#.....
O.....O..O..O...#..O..#O#.O..O...O....O#..O...#O.....O.OO...O....O..#...O....#O..#....O..O.##....OO.
.#.#..O........O...#.......O..##.O.###.O..O.....O.##O...OO....O..#..#O....O..O.O..........O...OO.O..
....O..O..O........#O.#.##...##....#.#.O...#O#.O....#.O#O#O....#.O#......O##..#.O.O....#O#..OO.#..#.
##....O...O###.O.....O#.OOO.O##.##....O.....O...O..O...O..#...O....##.....O........##...#.O...##O...
...O....###......#...O.OO........#.#.....OOO........O.#......O.O#....O.O.....#..##..O..#.#O#..O..O#O
.O..#.##O#...O.OO#...#OO.#..##.##..O.#.#O.O.#...OOOO...#.........O...........#..O.......#.##.O...##.
.OOO#.......OO....O..#..#O.O.O#.#O..#....O....#.O.O..O#..#...#.O.#O.#.OO.OO..#.#O.#.O#...#O.....#..#
...#O...O.O..#.O........O#.#....O.######O#...O.#.O.#..O.....#.....#...O..............#...O....##..#.
.O............O#......#O##O..OO......#....OO#..#..#..#OOO...#..#.....O#OO..O.O..#.O#..OO.##...O#.#..
.O...OOO.O.#........#..#..O.O.......O...#...#OO#O.....O...O......O...OO.O#.O.O#.OO.#......O.O....#O.
O.##O.....OO....O..##..O....#......O...O...O....####..#.....O.....O..O.#.O..#OO.#..#..O#O..O...#...O
..O...#O#...#.#..O...O#.O......O.#..#...#..#O..#...#..O.....O...OO.O#....OO.......#..###.OO..#..OOO.
.#..##O..O....O...O....O..O###.O.O......O#OO#O#O#O#...#...##.O.......#OOO#.##.#.O.....O.O.OO..#...O.
.O...#..O...O..O....#....O.....#O...#..O..#..#.......O...#..#....O.O#O....#....#O...OO...#.O.....OO#
.#.O..O............#...#...O..........O...O##......O.#....#O..O.O#...O##O.O..#....OOO..#...OOO....O.
O#O#.....O...OO##.....O#...O.....OO#.#...OO.O.O#.O.O.......#..##......O.#O.....#.O..#...#O...#...O..
..O##..#....O#.......OO#O.#......OO.##.#O.O.O....O.O..#O.#.....#..O......#O#....#O#.....#........#..
.O.##.#...O....#O........OOO.#O.....#.#....O..O..###....#.#..#.#O#.#.....#..#..#O##..#..OO.##.O....O
.O..O.O.....O.O...O#.#...##O....O.O.O...#....#O....#.O..OO...O.#..#O#........#OO....#...#.#..O..O...
...##O.O...O##....#..O...O#...#......#.OO##.....#..#.....O....#......O#.#O..O.#.O.O..O....O..O.O###O
...#....O.O...O..#.O....#...##O..O..O..#...O..#OO.#..O..#OO..O.........#O....#.#..O#O.O.#.O.....##O.
.......#.O.O.O..O##.............OO...O#O.O#.O..OO#.......O#...OOO.....#...O.......#.#..O#..O..OO#...
O...OO#.O..O.....OO......#.O#...#O#O.O......#.#O.....#..O.#.O#..#O.O....O.......O.....OO..O#....#.O.
..#...O#.O.O.O.#.O......O..#..O....#...#..O.O.#...#.....O..O....OO#OO.O.O.O..........#O..O#.O#..O...
......#O.....O.....OO.O..O#..#O###..O..#OO.#OO.....O.OOO..#.O...O....#O..#OO.#O...O.O....O#.....O.##
O.....O.O..#....O....##.....#.......OO#O.#...O..##...#....#.O#O..OO#.##.#.O.O.O.O#...#.OO.#O..OOOO#.
...OOO.#..#OO.O...#.....O#......#..O.O..OO#.O.O#.#.#........#.O.....#..O..O..#O..#O.#..#....#..#.O..
..O..O.....#.##.OO#.......O..OOO....OOO...#.O.#O...O...OO....O#OO...O.##....O.....#..O......#......O
.#..O..OO#O..#.##.O.O...##OOO.#...O......#O...O..#..#..#..O........#...O..#..#.OOO#.O.O......#.##O.#
#..#...O..#.O.#.....O..#.OO.#.....O.....#....O.OO.#O..#.#.#O..O....O.OO..O.......#O##..#O.#.OO...O..
O...O....OO..#OOOOO##.......##....#........O..O......O#O.#.......O.#.....OO........###..#........#.O
O.....O.......#OO.O.OO..O.O##.....O....O##......OO...O#O...O.....O.O....OOO#.O....#O.##...#.#..O##..
..O...#.....##.#O...#.OO.O#......O...O....OO..O.##O..OO#.O.#.O.O..#..#.O.O..O...O..#.OO.O.O....O....
O.OO.###.O..OO..##O....#.O......O.....O..OO......O.O.#OO...OO.#.....O#..O..#O.O........O.OO#O.OO....
O.....OO.....#O..O...O.#.OO#O.O##O...OO#..##O#.O.O#OO....#.#..#...##.#...#..O.O....O..O....#O.#.O...
...#.......OO.O..O......O.O.#....#..O.#.###.#......#.#O......#.#.O..O...O.#..#...#OO...O#.O....O##.O
....O.#...O..#.....O.#.OO..#...O.O....O....#..#...#..........O.O..#...O#...O#.#OOO.O.O.....O#O.....O
.....O...O.O...#.#....#....##.OO..#..O.O.OO...O#.O.....#..#...O...O......#.#....O..O......OO.O.O...#
.O.#..#.O..O...#.O.....OOO.O.#.OOO..O.........#.OO#....#.O.....#O.....#..#...O......#.#O.O...O.OOO.O
O#OO...O..#OO.OOO##..O........###..O....O#.O...O....O..#..........#...OO#O.....O.OO.O..#....O.#..#..
............O.O..O#...O.#......O....#.............O......#.O..O...O.#OO...#.....O....#.O#...#OO..O.#
.O.#.#O..#O...O.O..O#.O...##.#.#...O#...#..#.#OO#....#O....#......O.#O..O#O#.O....O.......#....#....
#.##...#.O.......#.....OO....#O#..O#.....O.#....O.#O#..O..##.#....O.......#....#.O#.#..#..O#.#..O.O.
..O..O#..O.O....O..#....O#.O##O..O..#.#OOO#O.O.##.O##O..........#.O.O#..#O.O.OO.#..OO...###O..#.O.##
.......O..........##..#.#.......#.O.O..O......O.O.OO.O............OO.O.O#..##.#......##O.O#O..O.....
....O......#..O..O..##O..O#.O....O..#.O.#...O.#O.O.O.O.#.#..O.....#..O.#..O#............O..#.O...#O#
..O...O..#O....O.#O..O.#.O.O..O..OO##.....##OO..#..#.O#O....O...#.....O#.O.#.......#.....O#..O..O.#.
.O..#...O..#.....O.#O#O....OOO..#..#.O..O.O.#......O.#OO#O..#.O#..#....O..#.O.O#......O#..##...OO..#
##.#...##.O...OOO....##O.O..OO#OO.O#...O.OO........#......OO...#.#..O#.#........O....OOO..O..O..O.#.
#.OOO....O......O....#.#.OO..#.....O...O.OO..O..OO.....OO........OO....O.O..#.O#.....O......#.#.#O..
...O........O..O.#O...#......O...O...O.....#.O....O.........#...OO....##...O.#.O.....O...O.......#O.
..O#.#O.OO#...O.O..O..OOO..........O.....#O....O......#..OO...O..O#O.#....#.O..........#O.OOO...##..
#..O#...OO#.O....O#......##.#O....O..OO.OO..O....#.......O.....O..O......O#O.....O..O...#....#....O.
.#....O............O.O.OO...O##O......#....O#.........OO.O#O............O##O.#....#O.O###.#O..#.....
O#.....O.O..O..#.....#.#....#......#...O.OO.#OO....#..##.O..O#O...OO..#...O.#.#.O..##.#....OO.O.....
#.....O......O#.#........#....O..#O.#O.OO..O.OO.O..O##.#.#.#OO....O.#....O.O..#.....#.....O.OO...OOO
..OO.##OO#O.............O.OO...O#.##...#.#O...#O.....#...#.......#OOO.#.O#OO.....#..O#..#...OO....#.
.#....OO.#.O##...#.O#.....OO#O...OOO..O##....OO.#.#.#......O#...O#OO....#......OOOOO#O...#..#.....O#
##O.O..O.##......#.OO...#...O..#O........##.O.......O#......#..#O....O....O#O.O..##.........O.......
..O.#...#OO#O....#O.....O...##.O....#..##O#........O..#..#..#...O..#.OO.#O#...O......#....#.......##
.O.###......#........##.....#...#...#O.O#O..........#..O.....O.OOO#O.....#...#.OO#O.O##O.OOO........
.#..O.......O....O...#.........#O##.OOO#O..#.#...O....O#O..O....#..O#..#....#O#......O#O#..#.....#.#
.###O.O..OO.O..O....O#.##O.O..O..O..#O#.#O#.O....O..O#..O..####.O...#..O..#OO....OO.......#..#.O..#.
O...O#...#.O....OO..##..O..O#O#.#OOO...OO...#..#....#O..#.#....#O...OO.O...O.#.O..#.#..O.O..O#.O#.#.
#.O..#..O##O..OOO.O...O.OO#.#...OO.OO.......O..#.O#OO....O.#O...........#...O..O...###O#..##..#.O.#.
.O.O.#.....O#...OO....#.....#.OOO.#..#O.#O.#O...#..O.....##..O#............O....O#...#.O#.....#OO.#.
##O.O...OO.O.#.#O..O....#.#.O............#O..O.....O..#..#.#.O..#.......#.O.........O.OO...#..#####.
.O##..####...#...........#.O..#..O#..OO........O..O...#O.##OO..#..O.O.O..#..##.O.OO#O#...#....#O.O.O
O.....O.O#....O#..#...O....OOO.OO..#..#......O...OOO.....O...O#..O..........####............#.O...OO
O#..O...#......#...#....#.#.O.........O...O....##O......#...O#.O.OO....#O.......#.O.O.OO.#O.#O...#OO
.O.....O...#.#..O#...O#.OO##O...#..#....#.O.O....O......#.O...##..O.##.....O#.O#..OO#.#.........#...
O....O.#O......O#O..OO#.#..#.OOO...#.#...#..#..OO..#........#.O..O..O##..OO#.#.O#OO.....#.O.##....O.
.OO............O....OO..#.#...O.#..O.......O.O......#....O..O..O#.......#.....OOO##...#.....O...O.#.
.#...O..OO.O....O...#.#...#OO#.O...#...##.O.......O.......#.....O..##O..O..OO..O#.OO..O.O...O.#...#.
..OO#.#O..#OO..O#O#O.O....O..O.......OO##.O..#.#O....O.#.....O..O.O....O##.#....#.#....O..#..#..OOO.
....#..O#..#...##.....#.#O.O......#....O##............#.....##O...#..O..##.#O..#O...O....O...##OO...
#O...O......O.O.#.OOO.....O##...#..O..OO...#..O#...O....O.O....#..O#...OOO..#.O..O....#..##.#.O.O...
##..#O#.O.#O...O#....OO...#..#.O##.O...#.O.#.O.O....O.#...O#.....####....OO.O..#.OO#....O...#..#....
O#..#...##.#.###.O##..#..##OO...#O#.........O.....O.OO#..OO..O....#.O#..........#...###.#......O..#.
O..#..##.O.O....OO.O#.##.O..O.#.#..#..O..OO..O...#.O.#....O#.....#OO...O.O#OO.O#.......OO#..#.O...O.
O..#..O#.#....#.O....O...#.OO.....O.O...O.#.###.#.O..O.O.#.....O.#......O#.....O...O......O.#..#...O
##O..#.##...#.......#.#..#.O....#.......O...O.##.O..#.O...O..##.O..#..O....O#....O.O#..O.......O.O.O
#..O...O....OO..O...O.OO....#..#..#.O#....#.#..O##.#..#.#.OOO#.#.O..#..O##......O.....OO....O#.#...O
#O.....O........##OO#..OO..O..O.#...O#......O..O..OO..OO....##.....#OOO.#OO.......O....O#.O...##..#.
.O..OO.O.....OOO...##O....##O....#.#.#O...OO.O...#..#......O.O.O..O.O..##....O....O.O.##....OO.#O.O.
..........O..O#...#...#..#..O..O...O#..O#OOO#......OOO#O..O.O.#O...O#..#O.OO..O##..O##O...O.O#.....#
#...#O..O.......O.O##.OO.#.#O..O.....O...#..O..O......O...#....#..O..O....##.....#.#...O.........#..
#....O.....O..O......#..#..........O..OO.#..##.....#..O...##....O.O..#.#O.#....OO.#....#.O...O...#O.
.......#..#.O..#....O......OOO.#....#O#.O..O..O#O#.##.#.#.#.............#O##OO.#.#O.#....O.O.#......""".split("\n")

data2 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split("\n")


data = [list(i) for i in data]

def up(data):
	flag = True

	while flag:
		flag = False
		for y in range(1,len(data)):
			for x in range(len(data[0])):
				if data[y][x] == "O" and data[y-1][x] == ".":
					data[y-1][x] = "O"
					data[y][x] = "."
					flag = True
	return data

data = up(data)

total = 0
for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x]=="O":
			total+=len(data)-y

print(total)

def leftdownright(data):
	flag = True

	while flag:
		flag = False
		for y in range(len(data)):
			for x in range(1,len(data[0])):
				if data[y][x] == "O" and data[y][x-1] == ".":
					data[y][x-1] = "O"
					data[y][x] = "."
					flag = True
	flag = True

	while flag:
		flag = False
		for y in range(len(data)-1):
			for x in range(len(data[0])):
				if data[y][x] == "O" and data[y+1][x] == ".":
					data[y+1][x] = "O"
					data[y][x] = "."
					flag = True
	flag = True

	while flag:
		flag = False
		for y in range(len(data)):
			for x in range(len(data[0])-1):
				if data[y][x] == "O" and data[y][x+1] == ".":
					data[y][x+1] = "O"
					data[y][x] = "."
					flag = True
	return data
	
previous = []
data = leftdownright(data)
cycles = 1
while data not in previous:
	previous.append(copy.deepcopy(data))
	data = leftdownright(up(data))
	cycles+=1

loopstart = previous.index(data)

loop = previous[loopstart:]
position = (1000000000-loopstart-1)%len(loop)
data = loop[position]

total = 0
for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x]=="O":
			total+=len(data)-y

print(total)
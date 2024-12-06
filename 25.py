import networkx as nx

data = """my input""".split("\n")

data = [i.split(": ") for i in data]
data = [(i[0],i[1].split(" ")) for i in data]


G = nx.Graph()

for i in data:
	for j in i[1]:
		G.add_edge(i[0],j)

cut_value, partition = nx.stoer_wagner(G)

print(len(partition[0])*len(partition[1]))

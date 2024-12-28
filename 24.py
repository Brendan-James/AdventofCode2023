import math
from sympy import *
#import vpython
data = """my input""".split("\n")

data = [[[int(k) for k in j.split(", ")] for j in i.split(" @ ")] for i in data]

testarea = (200000000000000,400000000000000)
testarea2 = (7,27)

extra = []

for i in data:
	x,y,z = i[0]
	vx,vy,vz = i[1]
	slope = vy/vx
	yintercept = (-(x/vx))*vy+y
	extra.append([slope,yintercept])

def intersect(a,b):
	global extra
	global data
	global testarea
	metaslope = extra[a][0]-extra[b][0]
	if metaslope == 0:
		return False
	metaintercept = extra[a][1]-extra[b][1]
	x = -metaintercept/metaslope
	y = extra[a][0]*(-metaintercept/metaslope)+extra[a][1]
	if not testarea[0]<x<testarea[1] or not testarea[0]<y<testarea[1]:
		return False
	if (data[a][0][0]>x and data[a][1][0]>0) or (data[a][0][0]<x and data[a][1][0]<0) or (data[b][0][0]>x and data[b][1][0]>0) or (data[b][0][0]<x and data[b][1][0]<0):
		return False
	return True

total = 0
for i in range(len(data)):
	for j in range(i+1,len(data)):
		if intersect(i,j):
			total+=1

print(total)

""" # visualization
for i in data[:3]:
	x,y,z = i[0]
	dx,dy,dz = i[1]
	normal = math.sqrt(dx**2+dy**2+dz**2)
	normal /= 300000000000000
	dx /= normal
	dy /= normal
	dz /= normal
	vpython.arrow(pos=vpython.vector(x,y,z),axis=vpython.vector(+dx,+dy,+dz),round=True,shaftwidth=1000000000000,headwidth=1500000000000,headlength=1000000000000)
"""

x, y, z, vx, vy, vz = symbols('x, y, z, vx, vy, vz', real=True)

equations = []

for i,v in enumerate(data[:5]):
	xn,yn,zn = v[0]
	vxn,vyn,vzn = v[1]
	tx = symbols("t"+str(i),real=True)
	equations.append(Eq(x+vx*tx,xn+vxn*tx))
	equations.append(Eq(y+vy*tx,yn+vyn*tx))
	equations.append(Eq(z+vz*tx,zn+vzn*tx))

# the magic box tells me the answer
print(solve(equations,domain=S.Reals))

print(404422374079783+199182431001928+166235642339249)

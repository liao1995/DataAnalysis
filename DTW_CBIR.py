from PIL import Image
from numpy import array
import os
import pprint
import mlpy
from collections import OrderedDict

data = {}
l = len(os.listdir("image"))
for fn in range(0, l-1):
	img = Image.open("image\\{0}.jpg".format(fn))
	arr = array(img)
	list = []
	for n in arr: list.append(n[0][0]) #R
	for n in arr: list.append(n[0][1]) #G
	for n in arr: list.append(n[0][2]) #B
	data[fn] = list
reference = data[31]
result = {}
for x,y in data.items():
	#print("{0} ----------------- {1}".format(x,y))
	dist = mlpy.dtw_std(reference, y, dist_only=True)
	result[x] = dist
sortedRes = OrderedDict(sorted(result.items(), key=lambda x: x[1]))
for a,b in sortedRes.items():
	print("{0} - {1}".format(a,b))

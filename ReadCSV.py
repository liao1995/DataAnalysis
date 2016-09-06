import csv
with open("pokemon.csv") as f:
	data = csv.reader(f)
	# Now we just iterate over the reader

	for line in data:
		print (""" id: {0} , Chinese Name: {1}, Janpese Name: {2}, 
		English Name: {3}, Property: {4}, Sort: {5}, Power: {6}, 
		Hit: {7}, PP: {8}""".format(line[0], line[1], line[2], line[3],
			line[4], line[5], line[6], line[7], line[8]))

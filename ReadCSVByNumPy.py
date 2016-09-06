import numpy as np
data = np.genfromtxt("pokemon.csv", 
		skip_header=1, 
		dtype=None, 
		delimiter=',')
print(data)

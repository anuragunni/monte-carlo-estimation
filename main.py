import numpy as np
import matplotlib.pyplot as plt

N = 100000
count = 0
i = 1

circlex = []
circley = []
squarex = []
squarey = []

while i <= N:
	x = np.random.uniform(-1,1)
	y = np.random.uniform(-1,1)

	if (x ** 2+y ** 2) < 1:
		circlex.append(x)
		circley.append(y)

	else:
		squarex.append(x)
		squarey.append(y)
	i += 1

print(4*(len(circlex))/N)
plt.plot(squarex, squarey, 'b.')
plt.plot(circlex, circley, 'g.')
plt.title("Estimating value of pi using Monte Carlo simulation")
plt.grid()
plt.show()
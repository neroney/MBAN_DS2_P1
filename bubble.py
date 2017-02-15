### Bubble chart

# add another dimension of data by changing the sizes

import random
import string
import matplotlib.pyplot as plt

N = 50
x = [random.random() for i in range(N)]
y = [random.random() for i in range(N)]
colors =  [random.random() for i in range(N)]
area =  [random.random()*1000 for i in range(N)] 

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()


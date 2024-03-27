import matplotlib.pyplot as plt
from random_walk import RandomWalk
rw = RandomWalk()

while True:

   rw.fill_walk()

   plt.style.use("bmh")
   fig,ax = plt.subplots()

   ax.scatter(rw.x_values, rw.y_values, c=rw.color, cmap=plt.cm.Blues, s=15 )

   plt.show()
   keep_running = input("Еще раз? (д/н): ")
   if keep_running == 'н':
       break
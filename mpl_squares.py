import matplotlib.pyplot as plt

input_value = list(range(1,1001))
squares = [x**2 for x in input_value]

plt.style.use("bmh")
fig, ax = plt.subplots()
#ax.plot(input_value, squares, linewidth=3)

ax.scatter(input_value,squares, s=10, c=squares , cmap=plt.cm.Blues)

ax.set_title("Значения квадратов", fontsize=14)
ax.set_xlabel("Значение", fontsize=14)
ax.set_ylabel("Квадрат", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

#print(plt.style.available)
ax.axis([1,1100,0,1100000])
#plt.show()
plt.savefig('squre.png', bbox_inches='tight')
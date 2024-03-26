import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

ax.set_title("Значения квадратов", fontsize=14)
ax.set_xlabel("Значение", fontsize=14)
ax.set_ylabel("Квадрат", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()
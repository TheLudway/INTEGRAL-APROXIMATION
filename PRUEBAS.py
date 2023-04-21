import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 1, 5, 3]
y2 = [5, 3, 2, 1, 4]

plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='red')
plt.fill_between(x, y1, color='gray', alpha=0.5)
plt.show()
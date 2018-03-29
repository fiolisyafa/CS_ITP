import matplotlib.pyplot as plt

numbers = list(range(1, 6))
cubes = [x**3 for x in numbers]

plt.scatter(numbers, cubes, c=cubes, cmap=plt.cm.Blues, edgecolor = 'none', s= 40)
plt.axis([0, 7, 0, 130])
plt.title("Cubes")
plt.xlabel('Numbers', fontsize=14)
plt.ylabel('Cubes', fontsize=14)
plt.show()

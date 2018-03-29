import matplotlib.pyplot as plt

print("initial_velocity(m/s) = 0")
print("speed_limit(m/s) = 60")
t = int(input("time(s): "))
a = int(input("acceleration(m/s2): "))
v = int(t) * int(a)

time = []
distance = []

for i in range(0, t+1):
    time.append(i)
    distance_travelled = 0.5 * int(a) * (int(i)**2)
    distance.append(distance_travelled)

print(time)
print(distance)

plt.scatter(time, distance, s=40)
plt.axis([0, 100, 0, 300])
plt.title('Driving Simulation', fontsize= 24)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Distance Travelled', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()

print("initial_velocity(m/s) = 0")
print("speed_limit(m/s) = 60")
t = int(input("time(s): "))
a = int(input("acceleration(m/s2): "))
s = int(input("distance(m): "))
v = int(t) * int(a)

for i in range(0, t+1):
    distance_travelled = 0.5 * int(a) * (int(i)**2)
    print("Duration:", i, " Distance: ", ("*" * int(int(distance_travelled)/int(10))))

if v <= 60:
    print("The person did not go over the speed limit. His/her maximum speed was", v, "m/s.")
else:
    print("The person went over the speed limit. His/her maximum speed was", v, "m/s.")

distance_travelled = 0.5 * int(a) * (int(t)**2)
if s > distance_travelled:
    print("The person did not reach the destination. He/she travelled", distance_travelled, "m.")
elif s <= distance_travelled:
    print("The person reached the destination. He/she travelled", distance_travelled, "m.")

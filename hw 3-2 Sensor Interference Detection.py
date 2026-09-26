N, D= input().split()
N = int(N)
D = int(D)
sensor = []
for i in range(N):
    (x,y,z,power) = input().split()
    sensor_data = (int(x), int(y), int(z), int(power))
    sensor.append(sensor_data)
itfPairs = set()
for i in range(N):
    (x1,y1,z1,power1) = sensor[i]
    for j in range(i+1, N):
        (x2,y2,z2,power2) = sensor[j]
        distanceSquare = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
        if distanceSquare <= D and power1 != power2:
            if sensor[i] < sensor[j]:
                itfPairs.add((sensor[i], sensor[j]))
            else:
                itfPairs.add((sensor[j], sensor[i]))
print(f"Interference Pairs: {len(itfPairs)}")
sortedPairs = sorted(itfPairs)
#print(type(sortedPairs))    A: list
for pair in sortedPairs:
    print(f"{pair[0]} <-> {pair[1]}")
'''for i in range(len(sortedPairs)):
    print(f"{sortedPairs[i][0]} <-> {sortedPairs[i][1]}")'''
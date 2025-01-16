import random

vector1 = [random.randint(0,100) for i in range (15)]
vector2 = [random.randint(0,100) for j in range (15)]

vector3 = []
for i in range(15):
    vector3.append(vector1[i] + vector2[i])

print(vector3)
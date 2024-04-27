import math
def euclideanDistance(p1, p2):
    x1, y1 =p1
    x2, y2 =p2
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2)

points = [(1,2),(4,6),(1,7),(-1,5),(2,-4),(0,3)]
distances = []
for i in range(len(points)):
    for j in range(i +1,len(points)):
        distances.append(euclideanDistance(points[i], points[j]))
print(min(distances))

import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b * b - 4 * a * c
x1 = int((b * (-1) + D ** (0.5)) / (2 * a))
x2 = int((b * (-1) - D ** (0.5)) / (2 * a))

print(x1)
print(x2)

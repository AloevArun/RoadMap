from math import sin, cos, tan, pi

x = float(input())

r = (x * pi) / 180

print(sin(r) + cos(r) + tan(r) ** 2)

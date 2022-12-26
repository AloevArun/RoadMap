from math import sqrt

a, b = float(input()), float(input())

s_ari = (a + b) / 2
s_geo = sqrt(a*b)
s_garm = (2 * a * b) / (a + b)
s_quad = sqrt((a ** 2 + b ** 2) / 2)

print(s_ari, s_geo, s_garm, s_quad, sep="\n")

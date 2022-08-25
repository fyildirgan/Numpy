# Numpy'da Koşullu İşlemler ( Conditions on Numpy)

import numpy as np
v = np.array([1, 2, 3, 4, 5])

#Klasik Döngü ile
ab = []

for i in v:
    if i < 3:
        ab.append(i)
print(ab)

#Numpy İle
#print(v < 3)
v[v < 3]
v[v > 3]
v[v != 3]
v[v >= 3]
print(v[v < 3])
print(v[v > 3])
print(v[v != 3])
print(v[v >= 3])


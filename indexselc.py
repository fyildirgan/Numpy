# Index Seçimi (Index Selection)
import numpy as np
a = np.random.randint(10, size=10)
print(a)
print(a[0])
print(a[0:5])
a[0] = 999
print(a[0])
print([a])
m = np.random.randint(10, size=(3, 5))
print(m)
m[2, 3] = 999
print(m[2, 3])
m[2, 3] = 2.9
print(m[2, 3])
print((m))
#bütün satıları seç :
print(m[:, 0])
print(m[1, :])
print(m)
print(m[0:2, 0:3])



#NUMPY: Bilimsel hesaplamalar için kullanılmaktadır.
#Arrayler ve çok boyutlu arrayler ve matrisler üzerinde yüksek performanslı
#çalışma imkanı sağlar.
#Verimli veri saklama ve vektörel operasyonlardır.
# Neden NumPy?

#import numpy as np
#a = [1, 2, 3, 4]
#b = [2, 3, 4, 5]
#ab = []
#Klasik liste yolu:
#for i in range(0, len(a)):
#    ab.append((a[i] * b[i]))
#print(ab)
#NumPy
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
print(a * b)


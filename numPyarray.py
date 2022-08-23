# NumPy Array'i oluşturmak(Creating Numpy Arrays)
import numpy as np

np.array([1, 2, 3, 4, 5])
print(np.array([1, 2, 3, 4, 5]))

# Girdiğin sayı adetince sayı oluşturuyor.
print(np.zeros(10, dtype=int))
# İnt ama belirli aralıklar olacak şekilde array oluşturma.
print(np.random.randint(0, 10, size=10))
# Belirli bir istatiksel dağılıma göre sayı üretmek istersek;
print(np.random.normal(10, 4, (3,4)))
# NumPy Array Özellikleri ( Attibutes of NumPy Arrays)

import numpy as np

#ndim : boyut sayisi
#shape : boyut bilgisi
#size : toplam eleman sayisi
#dtype: array veri tipi

a = np.random.randint(10, size=5)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
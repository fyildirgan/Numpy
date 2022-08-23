# Yeniden Şekillendirme(Reshaping)

import numpy as np
print(np.random.randint(1, 10, size=9).reshape(3, 3))
ar = np.random.randint(1, 10, size=9)
aa = ar.reshape(3, 3)
print(aa)
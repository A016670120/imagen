import numpy as np
import cv2
imagen = cv2.imread("corazon.jpg")
size  = imagen.shape
print (size)
nueva = np.array((size[0], size [1]), np.uint8)
for i in range (size [0]):
    for j in range (size[1]):
        #sacar cada pixel:
        px = imagen[i,j]
        print (f' pixel {i} {j} {px}') 
        p0 = .299
        p1 = .587
        p2 = .114
        nueva [i,j]= px [0]* p0 + px [1]* p1 + px [2] *p2
cv2.imwrite("nueva.jpg", nueva)


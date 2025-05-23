

" --------------------------------- "
# Görüntü Mantığı
" --------------------------------- "

import cv2
import numpy as np

img = np.zeros((10,10,3), dtype="uint8")
img[0,0]=[255,225,225]
img[0,1]=[255,225,200]
img[0,2]=[255,225,150]
img[0,3]=[255,225,15]

img= cv2.resize(img, (1000, 1000), interpolation=cv2.INTER_NEAREST)
print(img.shape)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

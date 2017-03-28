import cv2
import numpy as np

print cv2.__version__

img = cv2.imread('C:\Users\junjlin\Desktop\sample_doc_us.jpg',0)
cv2.imshow('myimage',img)
# img2 = cv2.copyMakeBorder(img)
print img.shape
print img.size
cv2.line(img, (0, 0), (902, 1293), (255, 0, 0), 10)
cv2.waitKey(0)
cv2.destroyAllWindows()


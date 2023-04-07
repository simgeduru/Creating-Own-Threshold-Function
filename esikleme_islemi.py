import cv2
import threshold

img_n = cv2.imread("C:\\Users\\Simge\\Desktop\\deneme14.jpg",0)

ret,thres=threshold.threshold_own(img_n,20,100)

cv2.imshow("original",img_n)
cv2.imshow("result", thres)

cv2.waitKey(0)
cv2.destroyAllWindows()
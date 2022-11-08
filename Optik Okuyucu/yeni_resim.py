import cv2 
img=cv2.imread('resim.jpg',0)
ret,th = cv2.threshold(img,125,255,cv2.THRESH_BINARY)

cv2.circle(th,(62,29),21,(0,0,0),-1)


cv2.imshow('2 kere işaretlenmiş',th)
cv2.imwrite('cift.jpg',th)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import time
sure1=time.time()
img=cv2.imread('resim.jpg',0)
print(img.shape)
ret,th = cv2.threshold(img,125,255,cv2.THRESH_BINARY)
cropped=th[3:-3,31:]
x=[31,93,155,217,279]
y=[26,78,130,182,234,286,338,390,442]
keys=[[0,0,0,0,1],[0,0,1,0,0],[0,0,0,1,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0]]
st_ans=[]
btrgb = cv2.cvtColor(cropped,cv2.COLOR_GRAY2RGB)
for i in y:
    k=keys[y.index(i)]
    n=0
    for j in x: 
        pixel=cropped[i,j]          
        if pixel==0:
            n+=1
    for j in x:
        s=k[x.index(j)]
        pixel=cropped[i,j]
        if pixel == 0 and s==1 and n==1:
            st_ans.append(1)
    if n==0:
        st_ans.append(0)
        cv2.circle(btrgb,(x[k.index(1)],i),20,(0,0,255),5)
    if n>1:
        st_ans.append(0)
        cv2.circle(btrgb,(x[k.index(1)],i),20,(0,0,255),5)

t=st_ans.count(1)
f=st_ans.count(0)
print('Doğru sayısı :',t,',yanlış sayısı :',f,'\n','Puan :',round(100/(t+f)*t,3))
cv2.imshow('Cevap Kagidi',img)
cv2.imshow('Cevap kagidi Kirpilmis',cropped)
cv2.imshow('Yanlis isaretlenen sorular',btrgb)
cv2.imwrite('son.jpg',btrgb)
cv2.waitKey(0)
cv2.destroyAllWindows() 
sure2=time.time()
print(sure2-sure1)

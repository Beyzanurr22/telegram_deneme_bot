import cv2
import numpy as np

img = np.zeros((500,500,3),dtype=np.uint8) +255
u1=(100,100)
u2=(100,300)
u3=(300,300)
cv2.line(img,u1,u2,(0,0,0),4)#(resim,baslangıc noktası,bitiş noktası,renk kalınlık)
cv2.line(img,u2,u3,(0,0,0),4)#(resim,baslangıc noktası,bitiş noktası,renk kalınlık)
cv2.line(img,u3,u1,(0,0,0),4)#(resim,baslangıc noktası,bitiş noktası,renk kalınlık)


#cv2.circle(img, (250,250),60,(255,0,0),4) #(resim,merkez,yarıçap,renk,kalınlık)

#cv2.rectangle(img,(130,130),(360,360),(0,255,0),2) #cizgi kalınlığını belirler ve kareyi olusturur

# cv2.line(img,  (100,100), (300,300), (0,0,255),thickness = 5) # çizgi çizme
# cv2.line(img,  (300,350), (400,500), (255,0,0),8)

# img = np.zeros((20,20,3),dtype=np.uint8) +255 #canvas = np.zeros((640,480,3),dtype=np.uint8) #canvas oluşturma

# img[0,0]=(0,0,0)
# img[0,1]=(50,0,0)
# img[0,2]=(100,0,0)
# img[0,3]=(150,0,0)
# img[0,4]=(200,0,0)
# img[0,5]=(250,0,0)

# img = np.zeros((20,20),dtype=np.uint8) +255 #canvas = np.zeros((640,480,3),dtype=np.uint8) #canvas oluşturma

# img[0,0]=(255)
# img[0,1]=(200)
# img[0,2]=(150)
# img[0,3]=(100)
# img[0,4]=(50)
# img[0,5]=(0)


#img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)
 # canvas boyutunu ayarlama

cv2.imshow("pencere",img)# pencereyi gösterme
cv2.waitKey(0) # bekleme
cv2.destroyAllWindows() # pencereyi kapatma
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#imp_img=cv2.VideoCapture("rohi.jpg")
#res,img=imp_img.read()
img=cv2.imread("rohi.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(gray,1.1,5)
for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w),(255,255,0),2)
cv2.imshow("ELONE IMAGE",img)
cv2.waitKey(0)
#img.release()
cv2.destroyAllWindows()
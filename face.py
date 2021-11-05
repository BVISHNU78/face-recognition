import cv2
import face_recognition
trained_data=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
#img=cv2.imread('0 (510).jpg')
webcam=cv2.VideoCapture(0)
while True:
    ret,frame=webcam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=trained_data.detectMultiScale(gray)
    for(x,y,w,h)  in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),10)
        cv2.imshow('hello',frame)
        if cv2.waitKey(1)& 0xFF == ord('q'):
            break
webcam.release()
cv2.destroyAllWindows()


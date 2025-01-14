import cv2
import numpy as np
import os
import RPi.GPIO as GPIO
from gpiozero import Servo, LED
from time import sleep
from pymongo import MongoClient
from datetime import datetime
from bson.binary import Binary

#GPIO setup
led = LED(23) 
led.off()
Button = 18
servo = Servo(5)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Button,GPIO.IN)
#db setup
mongodb = MongoClient("mongodb://192.168.0.5:27017/")
db = mongodb.full_house
#camera setup
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0
# names related to ids: example ==> loze: id=1,  etc
# 이런식으로 사용자의 이름을 사용자 수만큼 추가해준다.
names = ['None', 'robert', 'ljy', 'chs', 'ksw']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)


def holdsignal(Button): #채터링 방지
    b = GPIO.input(Button)
    sleep(5)
    return b

def btncheck(): #버튼 신호 flag
    currentstate = 0
    while 1:
        if holdsignal(Button) == 1: #안눌렀을때            
            print("off")
            currentstate = 0
            led.off()
        else:
            print("on")
            currentstate = 1                    
            led.on()
            return currentstate
    
def face_detect():    
    if btncheck() == 1: # 스위치를 누른 경우
        
        while 1:
      

                ret, img =cam.read()
                img = cv2.flip(img, 1) # Flip vertically
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
                faces = faceCascade.detectMultiScale( 
                    gray,
                    scaleFactor = 1.2,
                    minNeighbors = 5,
                    minSize = (int(minW), int(minH)),
                    )
                for(x,y,w,h) in faces:
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                    id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # Check if confidence is less them 100 ==> "0" is perfect match
                    if (confidence > 15 and confidence < 100):
                        id = names[id]
                        confidence = "  {0}%".format(round(100 - confidence))
                        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
                        servo.max() #문열림 동작
                        sleep(10)
                        servo.min()
                        print("문열림")
                        return 0
                                                                                   
                    else:
                        id = "unknown"
                        confidence = "  {0}%".format(round(100 - confidence))
                        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
                        binary_value = Binary(img) #사진을 바이너리 형태로 db에 저장
                        doc = {
                            "reg_date" : datetime.now(),
                            "picture" : binary_value,
                            
                        }
                        db.camera.insert_one(doc)

                cv2.imshow('camera',img) 
                
                k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video                
                if k== 27:
                    break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()    


if __name__ == "__main__":
    face_detect()
import cv2
import numpy as np
import os
import sqlite3
from PIL import Image
from threading import Thread
import pyttsx3
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer\\trainningData.yml')

engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
text=""
label=""
def voice():
    global label,name
    # sleep(5)
    if (label!=name):
        label=name
        
        text="Xin Chào "+name
        engine.say(text)
        engine.runAndWait()
    return
def getProfile(id):
    conn=sqlite3.connect('data.db')
    query="SELECT * FROM people WHERE ID =" + str(id)
    cusros=conn.execute(query)
    profile=None
    for row in cusros:
        profile=row
    conn.close()
    return profile

cap=cv2.VideoCapture(0)
fontface=cv2.FONT_HERSHEY_SIMPLEX
while(True):
    ret, frame =cap.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        id,confidence=recognizer.predict(roi_gray)         
       
        if confidence<40: 
            profile=getProfile(id)
            if (profile !=None):
                cv2.putText(frame,"" +str(profile[1]),(x+10,y+h+30),fontface,1,(0,255,0),2)
                name=str(profile[1])
                
                    
        else:
            cv2.putText(frame,"Unknown",(x+10,y+h+30),fontface,1,(0,255,0),2)
           
    
    thread = Thread(target=voice)
    thread.start()
    cv2.imshow('image',frame)
    if (cv2.waitKey(1)==ord('q')):
        break;


cap.release()
cv2.destroyAllWindows()

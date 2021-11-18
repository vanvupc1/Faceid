import cv2
import numpy as np
import os
import sqlite3
from PIL import Image
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer\\trainningData.yml')
def getProfile(id):
    conn=sqlite3.connect('data.db')
    query="SELECT * FROM people WHERE ID =" + str(id)
    cusros=conn.execute(query)
    profile=None
    for row in cusros:
        profile=row
    conn.close()
    return profile
fontface=cv2.FONT_HERSHEY_SIMPLEX
def main():
    image_path = "2.jpg"
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray)
    print('Found {0} faces!'.format(len(faces)))
    # Draw a rectangle around the faces
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        id,confidence=recognizer.predict(roi_gray)
        profile=getProfile(id)
        id,confidence=recognizer.predict(roi_gray)
        if confidence<80: 
            profile=getProfile(id)
            if (profile !=None):
                cv2.putText(image,"" +str(profile[1]),(x+10,y+h+30),fontface,1,(0,255,0),2)
        else:
            cv2.putText(image,"Unknown",(x+10,y+h+30),fontface,1,(0,255,0),2)
        cv2.imshow("Faces found", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

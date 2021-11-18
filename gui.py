from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from time import sleep
from threading import Thread, stack_size
import sqlite3
import pyttsx3
import os
import numpy as np
from tkinter import messagebox
engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
window = Tk()
window.title("Face Id")
# window.geometry("900x600")
video = cv2.VideoCapture(0)
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH) 
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
canvas = Canvas(window, width = canvas_w, height= canvas_h , bg= "red")
canvas.grid(column=1,row=1)
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
fontface=cv2.FONT_HERSHEY_SIMPLEX
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer\\trainningData.yml')
label=""
name=""
# Lấy thông tin từ database
def getProfile(id):
    conn=sqlite3.connect('data.db')
    query="SELECT * FROM people WHERE ID =" + str(id)
    cusros=conn.execute(query)
    profile=None
    for row in cusros:
        profile=row
    conn.close()
    return profile
# trợ lý ảo thông báo
def voice():
    global label,name
    # sleep(5)
    if (label!=name):
        label=name
        text="Xin Chào "+name
        engine.say(text)
        engine.runAndWait()
    return



def detect():
    global canvas, photo,label,name
    ret, frame = video.read()
    # Ressize
    frame = cv2.resize(frame, dsize=None, fx=1, fy=1)
    # Chuyen he mau
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        id,confidence=recognizer.predict(roi_gray)         
       
        if confidence<50: 
            profile=getProfile(id)
            if (profile !=None):
                cv2.putText(frame,"" +str(profile[1]),(x+10,y+h+30),fontface,1,(0,255,0),2)
                name=str(profile[1])
                
        else:
            cv2.putText(frame,"Unknown",(x+10,y+h+30),fontface,1,(0,255,0),2)
            
        

    # Convert hanh image TK
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    # Show
    canvas.create_image(0,0, image = photo, anchor=tkinter.NW)
    thread = Thread(target=voice)
    thread.start()
    window.after(20,detect)



    

detect()

window.mainloop()
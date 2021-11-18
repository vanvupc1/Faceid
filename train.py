import cv2
import numpy as np
import os
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create()
path ='dataset'

# Lấy ảnh với ID :
def getImagerWithID(path):
    # Lấy tất cả các file trong thư mục
    imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
    # Tạo mảng faces rỗng
    faces=[]
    # tạo mảng Id rỗng
    IDs=[]
    # vòng lập lấy id 
    for imagepath in imagepaths:
        # loading ảnh và convert ảnh sang dạng gray scale
        faceImg=Image.open(imagepath).convert('L')
        # Chuyển đổi ảnh sang mảng Numpy
        faceNp=np.array(faceImg,'uint8')
        # cắt Id của ảnh
        Id=int(imagepath.split('\\')[1].split('.')[1])
        # Thêm mảng numpy faceNp vào mảng faces
        faces.append(faceNp)
        # thêm id đi cùng với khuôn mặt 
        IDs.append(Id)
    return faces,IDs


faces , IDs=getImagerWithID(path)
recognizer.train(faces,np.array(IDs))
recognizer.save('recognizer/trainningData.yml')

cv2.destroyAllWindows()

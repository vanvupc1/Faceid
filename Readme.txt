Face ID
Cài đặt các thư viện và cài đặt SQlite
pip install opencv-python
pip install numpy
pip install sqlite
pip install pillow
Hướng dẫn sử dụng:
Chuẩn bị data để train
  -chạy file data.py
       -Nhập ID và Name của data
	-Xuất hiện frame để set data là 100 tấm khuôn mặt data cần chuẩn bị train
Train dữ liêu:
  -Chạy file train.py
     trong train sẽ tự động cắt id của những bức ảnh chứa khuôn mặt đã được lưu trian thành một ma trận
Thực hiện nhận diện khuôn mặt:
  -Chạy file main.py để thực hiện nhận diện khuôn mặt bằng Webcam
  -Chạy file faceid.py để nhận diện khuôn mặt bằng ảnh.
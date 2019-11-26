#!/usr/bin/env python
# coding: utf-8
# -*- coding:utf-8 -*-
import sys
import face_recognition 
import cv2

print("检测目标文件路径："+sys.argv[1])
location_1 = sys.argv[1]

i = 0
normal_known_faces = []
while(1 == 1):
    try:
        # 加载已知图片
        known_image = face_recognition.load_image_file("normal/image"+str(i)+".jpg")
        # 对图片进行编码，获取128维特征向量
        image_encoding = face_recognition.face_encodings(known_image)[0]
        # # 存为数组以便之后识别
        normal_known_faces.append(image_encoding)
        i = i + 1
    except(FileNotFoundError):
        print("正常文件扫描结束")
        break

j = 0
warning_known_faces = []
while(1 == 1):
    try:
        # 加载已知图片
        warning_known_image = face_recognition.load_image_file("warning/image"+str(j)+".jpg")
        # 对图片进行编码，获取128维特征向量
        warning_image_encoding = face_recognition.face_encodings(warning_known_image)[0]
        # # 存为数组以便之后识别
        warning_known_faces.append(warning_image_encoding)
        j  = j + 1
    except(FileNotFoundError):
        print("警告文件扫描结束")
        break

# 加载待识别图片
unknown_image = face_recognition.load_image_file(location_1)

# 初始化一些变量
face_locations = []
face_encodings = []
frame_number = 0

# 获取人脸区域位置
face_locations = face_recognition.face_locations(unknown_image)
# 对图片进行编码，获取128维特征向量
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

for face_encoding in face_encodings:
    result = None
    # 识别图片中人脸是否匹配已知图片
    warning_match = face_recognition.compare_faces(warning_known_faces, face_encoding, tolerance=0.5)
    if warning_match[0]:
        result = "warning_mayun"
    else:
        result = 'Unknown'

    if result == 'Unknown':
        normal_match = face_recognition.compare_faces(normal_known_faces, face_encoding, tolerance=0.5)
        if normal_match[0]:
            result = "normal_zhang bozhi"
        elif normal_match[1]:
            result = "normal_liudehua"
        elif normal_match[2]:
            result = "normal_liuyifei"
        else:
            result = 'Unknown'

    print("检测结果：" + result)

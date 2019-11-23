# -*- coding:utf-8 -*-
"""
Created on Thu Oct 31 20:17:22 2019 

@author: admin
"""
import face_recognition
import cv2

# 加载已知图片
known_image_cc = face_recognition.load_image_file("liudehua.jpg")
known_image_xy = face_recognition.load_image_file("zhangbozhi.jpg")
known_image_smy = face_recognition.load_image_file("liuyifei.jpg")
known_image_zch = face_recognition.load_image_file("mayun.jpg")

# 对图片进行编码，获取128维特征向量
caocao_encoding = face_recognition.face_encodings(known_image_cc)[0]
xy_encoding = face_recognition.face_encodings(known_image_xy)[0]
zys_encoding = face_recognition.face_encodings(known_image_smy)[0]
cyz_encoding = face_recognition.face_encodings(known_image_zch)[0]
# 存为数组以便之后识别
known_faces = [caocao_encoding, xy_encoding, zys_encoding, cyz_encoding]

# 加载待识别图片
unknown_image_1 = face_recognition.load_image_file(r".\unknow\liudehua2.jpg")
unknown_image_2 = face_recognition.load_image_file(r".\unknow\zhangbozhi2.jpg")
unknown_image_3 = face_recognition.load_image_file(r".\unknow\liuyifei2.jpg")
unknown_image_4 = face_recognition.load_image_file(r".\unknow\mayun2.jpg")
unknown_faces = [unknown_image_1, unknown_image_2, unknown_image_3, unknown_image_4]

# 初始化一些变量
face_locations = []
face_encodings = []
face_names = []
frame_number = 0
for frame in unknown_faces:
    face_names = []
    # 获取人脸区域位置
    face_locations = face_recognition.face_locations(frame)
    # 对图片进行编码，获取128维特征向量
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # 识别图片中人脸是否匹配已知图片
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.5)
        name = None
        if match[0]:
            name = "liudehua"
        elif match[1]:
            name = "zhang bozhi"
        elif match[2]:
            name = "liuyifei"
        elif match[3]:
            name = 'mayun'
        else:
            name = 'Unknown'
        face_names.append(name)

        # 结果打上标签
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # 绘制脸部区域框
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # 在脸部区域下面绘制人名
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # 显示图片
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow("face recognition.jpg", image_rgb)
        cv2.waitKey(0)

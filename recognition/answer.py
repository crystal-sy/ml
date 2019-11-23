import sys
import face_recognition
import cv2

print("检测目标文件路径："+sys.argv[1])
location_1 = sys.argv[1]

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
unknown_image = face_recognition.load_image_file(location_1)

# 初始化一些变量
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

# 获取人脸区域位置
face_locations = face_recognition.face_locations(unknown_image)
# 对图片进行编码，获取128维特征向量
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

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
        cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 0, 255), 2)
        # 在脸部区域下面绘制人名
        cv2.rectangle(unknown_image, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(unknown_image, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # 显示图片
        image_rgb = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)
        cv2.imshow("face recognition.jpg", image_rgb)
        cv2.waitKey(0)
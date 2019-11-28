from PIL import Image

# im = Image.open("/Users/likai/Desktop/workspace/ml/server/upload/upload_1c9e76856b20672b177fbfa61f9c5d5e.jpeg")
# im.thumbnail((640,620))
# print(im.format, im.size, im.mode)
# im.save("./test.jpg")

im = Image.open("/Users/likai/Desktop/workspace/ml/server/upload/upload_1c9e76856b20672b177fbfa61f9c5d5e.jpeg")

size = im.size

print (size)

if size[0] > size[1]:
    rate = float(1000) / float(size[0])
else:
    rate = float(750) / float(size[1])
new_size = (int(size[0] * rate), int(size[1] * rate))
new = im.resize(new_size, Image.BILINEAR)
new.save('new2.jpg')
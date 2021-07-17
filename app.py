#pip install opencv-python
import cv2

pic1 = cv2.imread(filename='pic1.jpg')
pic2 = cv2.imread(filename='pic2.jpg')

height = min(pic1.shape[0], pic2.shape[0])
width = min(pic1.shape[1], pic2.shape[1])
depth = 3

pic1_resize = cv2.resize(src=pic1, dsize=(width, height))
pic2_resize = cv2.resize(src=pic2, dsize=(width, height))

#brightness
alpha = 0.4
beta = 0.6

blend_pic = cv2.addWeighted(src1=pic1_resize, alpha=alpha, src2=pic2_resize, beta=beta, gamma=0)

cv2.imwrite(filename='finaly.jpg', img=blend_pic)

cv2.imshow(winname='window_blend', mat=blend_pic)
cv2.waitKey()

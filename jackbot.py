from PIL import ImageGrab, ImageOps
import numpy as np
from pynput.keyboard import Key,Controller
import time,cv2

kkey = Controller()
# y1=400
# y2=410
y1=360
y2=370
box = ((850,y1,860,y2),(1060,y1,1070,y2))

def img():
	image = []
	for x in box:
		image.append(ImageGrab.grab(x))

	grayImage = []
	for x in image:
		grayImage.append(ImageOps.autocontrast(x))

	arr = []
	for x in grayImage:
		arr.append(np.array(x))

	# for x in arr:
	# 	print(x.sum(),end="   ")
	# print("")
	return arr
def main():
	posisi = "kiri"
	while True:
		box = img()
		print(box[0].sum())
		if box[0].sum()<71300:
			posisi = "kanan"
		if box[1].sum()<71300:
			posisi = "kiri"
		if posisi=="kanan":
			kkey.press(Key.right)
			kkey.release(Key.right)
			# time.sleep(0.04)
		if posisi=="kiri":
			kkey.press(Key.left)
			kkey.release(Key.left)
			# time.sleep(0.04)
if __name__ == '__main__':
	main()
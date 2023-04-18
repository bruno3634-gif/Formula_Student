import cv2
import numpy as np





def inv(x):
    return x[:,::-1]



video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

video.set(cv2.CAP_PROP_FRAME_WIDTH , 800)
video.set(cv2.CAP_PROP_FRAME_HEIGHT , 800 )

print("Camara iniciada.")
ret,frame = video.read()

"""
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
print(gray)
print(gray.shape)
cv2.imshow("gray original",gray)
gray = inv(gray)
print(gray)
print(gray.shape)
cv2.imshow("gray",gray)"""



while True:
    ret,frame = video.read()
    frame_inv = inv(frame)
    cv2.imshow("Camara PC",frame);
    cv2.imshow("gray original",frame_inv)
    if cv2.waitKey(1)== ord('q'):
        break




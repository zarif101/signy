import cv2
import numpy as np
import plaidml.keras
plaidml.keras.install_backend()
from keras.models import Sequential
from keras.models import load_model
import time

model = load_model('sign_language_thresh.h5')
pred = 'None'
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (180,180)
fontScale              = 3
fontColor              = (255,0,0)
lineType               = 2

cv2.namedWindow('frame')
def get_sign(event,x,y,flags,param):
    global pred
    if event == cv2.EVENT_LBUTTONDOWN:
        pic = frame[205:305,140:225]
        pic = cv2.resize(pic,(28,28))
        pic = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
        pic = np.reshape(pic,(1,28,28,1))
        print(model.predict_classes(pic))
        pred = str(model.predict_classes(pic))

cap = cv2.VideoCapture(0)

cv2.setMouseCallback('frame',get_sign)
while True:
    ret, frame = cap.read()
    cv2.rectangle(frame,(140,225),(205,305),(200,200,100),1)
    cv2.putText(img=frame,text=pred,
        org=bottomLeftCornerOfText,
        fontFace=font,
        fontScale=fontScale,
        color=fontColor,
        thickness=lineType)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

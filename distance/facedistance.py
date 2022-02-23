import cv2
import cvzone
from  cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

textList = ["Herr Reichspräsident!", "Abgeordnete, ", "Männer und Frauen des","Schwere Sorgen lasten", "seit Jahren auf unserem ", "Nach einer Zeit stolzer ", "eichen Blühens und Gedeihens"]

while True:
    sucess, img = cap.read()
    imgText = np.zeros_like(img)

    if sucess:
        img, face = detector.findFaceMesh(img, draw=False)
        if face:
            face = face[0]
            lefteye = face[145]
            righteye = face[374]
            #cv2.circle(img, lefteye, 5, (255, 255, 0), cv2.FILLED)
            #cv2.circle(img, righteye, 5, (255, 255, 0), cv2.FILLED)

            cv2.line(img, lefteye, righteye, (0, 200, 0), 2)

            w, _ = detector.findDistance(lefteye,righteye)


            W = 7.9
            #d = 50
            #f = (w*d)/W
            #print(f)

            #distance calculate

            f = 700
            d = (W*f)/w
            print(d)

            cvzone.putTextRect(img, f'Distance:{int(d)}cm', (face[10][0], face[10][1]), scale=2)
            for i, text in enumerate(textList):
                singleHeight = 20 + int(d/5)
                scale = 0.4 + d/100
                cv2.putText(imgText, text, (50, 50 + (i*singleHeight)), cv2.FONT_ITALIC, scale, (255, 255, 255), 2)
        imgStacked = cvzone.stackImages([img, imgText], 2, 1)
        cv2.imshow("Image", imgStacked)
        cv2.waitKey(1)

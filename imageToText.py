import re
import numpy as np
import cv2
import time
import json
import base64
import requests

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
ret,frame = cap.read()
cap.release()
#Convert image to sendable format and store in JSON

image = cv2.imread("people.png")
ret,image = cv2.imencode(".png",image)
image = image.tobytes()
encodedString = base64.b64encode(image).decode("utf-8")
with open("output0.txt","w") as textFile:
    textFile.write(encodedString)


#ret , encimg = cv2.imencode(".png ", frame)
imageFile = open("people.png","rb")
encodedString = base64.b64encode(imageFile.read()).decode("utf-8")
with open("output.txt", "w") as textFile:
    textFile.write(encodedString)

# img_byte = base64.b64encode(img_str).decode("utf-8")
# img_json = json.dumps({'image': img_byte}).encode('utf-8')


# #Send HTTP request
# response = requests.post("http://localhost:6868/api/image", data=img_json)
# print(response.text)

# #print('{0} {1}'.format(response.status_code, json.loads(response.text)))
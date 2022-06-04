
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
ret , encimg = cv2.imencode(".png ", frame)
img_byte  = encimg.tobytes()
img_str = base64.b64encode(img_byte).decode("utf-8")
img_json = json.dumps({'image': img_str}).encode('utf-8')


#Send HTTP request
response = requests.post("http://localhost:6868/api/image", data=img_json)
print(response.text)

#print('{0} {1}'.format(response.status_code, json.loads(response.text)))
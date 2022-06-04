from time import sleep
from cv2 import imshow
from flask import Flask, render_template, Response, request
import cv2
import numpy as np
from flask_cors import CORS, cross_origin
import json
import base64

import person 

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template("pic.html",title="Home")



@app.route('/api/human_detect', methods=['POST'])
@cross_origin()
def save_image():
    #Data conversion process
    data = request.data.decode('utf-8')
    data_json = json.loads(data)
    image = data_json['image']
    image_dec = base64.b64decode(image)
    data_np = np.fromstring(image_dec, dtype='uint8')
    decimg = cv2.imdecode(data_np, 1)

    # filename = "./images/image{}.png ".format(6868)
    # cv2.imwrite(filename, decimg)
    # image = cv2.imread("image.jpg")
    detection = person.human_detection(decimg)
    dictionary = {"numbersOfHumans":detection["numbersOfHumans"]}
    #Send HTTP response
    response=json.dumps(dictionary)
    return Response(response)

if __name__ == '__main__':
    person.loadModel()
    print("model loaded")
    app.run(host='0.0.0.0', port=6868)



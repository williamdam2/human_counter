import cv2
import numpy as np
net = any
classes = None
def loadModel():
    global net
    global classes
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    
    with open("yolov3.txt", 'r') as f:
        classes = [line.strip() for line in f.readlines()]

def get_output_layers():
    global net
    layer_names = net.getLayerNames()

    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers

def human_detection(image):
    global net
    global classes

    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392
    
    

    blob = cv2.dnn.blobFromImage(image, scale, (608, 608), (0, 0, 0), True, crop=False)

    net.setInput(blob)

    outs = net.forward(get_output_layers())

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.4
    nms_threshold = 0.5

    # Thực hiện xác định bằng HOG và SVM


    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            if(class_id==0):
                confidence = scores[class_id]
                if confidence > 0.4:
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    detec_info = {"numbersOfHumans":len(indices)}

    return detec_info
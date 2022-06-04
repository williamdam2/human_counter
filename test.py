from json import detect_encoding
import person
import cv2
image = cv2.imread("image.jpg")

#cv2.imshow("image",image)
detected = person.human_detection(image)
print(detected)
print(detected["numbersOfHumans"])
# cv2.waitKey()
# cv2.destroyAllWindows()
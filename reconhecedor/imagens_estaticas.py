import cv2
from mtcnn import MTCNN
detector = MTCNN()
import os

local = os.listdir('/home/tarsila/projetos/reconhecimentofacial/images/tarsila')
print(os.path.abspath(local[0]))

image = cv2.cvtColor(cv2.imread(os.listdir(os.path.abspath(local[0]))), cv2.COLOR_BGR2RGB)
result = detector.detect_faces(image)

# Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
bounding_box = result[0]['box']
keypoints = result[0]['keypoints']

cv2.rectangle(image,
              (bounding_box[0], bounding_box[1]),
              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              (0,155,255),
              2)

cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

cv2.imwrite("/home/tarsila/projetos/reconhecimentofacial/faces/tarsila/t1_draw.jpg", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

print(result)
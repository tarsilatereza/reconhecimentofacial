import cv2
from mtcnn import MTCNN
detector = MTCNN()
import os

# CAMINHOS DE IMAGENS
# path = 'a'
# path_faces = 'a'
while True:
    def load_images(path, path_faces):
        local_images = ''
        local_faces = ''
        print(path) #imagens
        print(path_faces) #faces
        local_images = path
        local_faces = path_faces
        #for filename in os.listdir(directory_images):
        #   path = directory_images + filename
        #   path_faces = directory_faces + filename
    def load_dir(directory_images, directory_faces):
        for root, dirs, files in os.walk(directory_images):
            for d in dirs:
                path = os.path.join(root, d) + '/'
                path_faces = directory_faces + '/' + d + '/'
                load_images(path, path_faces)
    if __name__ == '__main__':
        load_dir('/home/tarsila/projetos/reconhecimentofacial/images',
            '/home/tarsila/projetos/reconhecimentofacial/faces')
    # images_local = '/home/tarsila/projetos/reconhecimentofacial/images/'
    # people_images = os.listdir('/home/tarsila/projetos/reconhecimentofacial/images/')
    # print(f'Encontramos imagens de {people_images}.')
    # question = str(input('De qual pessoa você quer extrair o rosto? ')).lower().strip()
    # teste = images_local+question
    # print(teste)
    
    image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
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

    cv2.imwrite(path_faces, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(5) == ord('q'): # o tempo é contado em milisegundos
            break # se apertar a tecla 'q', o programa para
print(result)
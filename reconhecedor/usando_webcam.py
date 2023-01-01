import cv2 #openCv
import mediapipe as mp # chamar mediapipe de mp a partir de agora

# PARA WEBCAM

# incializar OpenCv
webcam = cv2.VideoCapture(0) # esse índice simboliza qual webcam usar. duas webcams = 0 e 1

# inicializar MediaPipe
face_recognition_solution = mp.solutions.face_detection # usando a solução que já está pronta da biblioteca do mediapipe
recognition_faces = face_recognition_solution.FaceDetection() # cria o reconhecedor que usa a solução
drawing = mp.solutions.drawing_utils # vai desenhar pontos para confirmar que o reconhecedor está funcionando


while True: # é necessário um loop para o programa ir reconhecendo os frames continuamente e não só uma vez, não só em uma imagem.
	
	# 1) lendo as informações da webcam
	checker, frame = webcam.read() # checker é um verdadeiro ou falso, verificar se conseguiu armazenar e frame é o que ele conseguiu armazenar, a imagem
	if not checker:
		print('Não estou conseguindo armazenar informação')
		break

	# 2) reconhecendo os rostos que estão no frame, na informação armazenada
	faces_list = recognition_faces.process(frame) 
	if faces_list.detections:
		for face in faces_list.detections:
			# desenhando pontinhos na imagem
			drawing.draw_detection(frame, face)
	cv2.imshow(f'rostos identificados', frame) # ferramenta do OpenCv para apresentar ao usuário o programa rodar

	# autra ferramenta do OpenCv, permite configurar uma tecla para parar o loop
	if cv2.waitKey(5) == ord('q'): # o tempo é contado em milisegundos
		break # se apertar a tecla 'q', o programa para
webcam.release() # fecha a webcam
cv2.destroyAllWindows() # fecha todas as janelas que possam vir a estar abertas

import os

def load_images(path, path_faces):
	print(path) #imagens
	print(path_faces) #faces
	print(type(path))
	#for filename in os.listdir(directory_images):
	#	path = directory_images + filename
	#	path_faces = directory_faces + filename


def load_dir(directory_images, directory_faces):
	for root, dirs, files in os.walk(directory_images):
		for d in dirs:
			path = os.path.join(root, d) + '/'
			path_faces = directory_faces + '/' + d + '/'
			load_images(path, path_faces)
if __name__ == '__main__':
	load_dir('/home/tarsila/projetos/reconhecimentofacial/images',
		'/home/tarsila/projetos/reconhecimentofacial/faces')

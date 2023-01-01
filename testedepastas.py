import os # andar pelas pastas 
#print(os.path.abspath('..')) # procura o caminho deste diretório
#print(os.listdir('..')) # lista o que tem nesse diretório

# r_path = './faces'
# for root, subFolder, fileName in os.walk(r_path):
#   for folder in subFolder:
#     print(folder)

local = os.listdir('/home/tarsila/projetos/reconhecimentofacial/images/tarsila')
print(os.path.abspath(local[0]))


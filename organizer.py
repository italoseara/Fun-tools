import os
import shutil

os.chdir(r'C:\Users\anejo\OneDrive\Área de Trabalho\organizer')
while True:
    files = os.listdir()
    if len(files) != 0:
        for file in files:
            file_name = file[:file.find('.')].split(' ')

            try:
                os.mkdir(f'C:\\Users\\anejo\\OneDrive\\Área de Trabalho\\organized\\{file_name[0]}')
                print(f'Criando pasta {file_name[0]}')
            except:
                print(f'Pasta {file_name[0]} já existente')

            shutil.move(file, f'C:\\Users\\anejo\\OneDrive\\Área de Trabalho\\organized\\{file_name[0]}\\{file}')
            print(f'Movendo arquivo {file}')
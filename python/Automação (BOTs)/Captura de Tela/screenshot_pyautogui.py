# Tira screenshots da tela ao apertar uma tecla e guarda em diretório próprio

from pyautogui import screenshot as pagScreenshot
from keyboard import wait as keyboardWait
from os import mkdir as osMkdir
from os.path import exists as osPathExists

trigger = 'F2'
path = '/'.join(str(__file__).split('\\')[:-1]) + '/screenshots' # Diretório dos screenshots

rg = ((1920-640)/2, # Centraliza eixo X
      (1080-640)/2, # Centraliza eixo Y
      640,
      640) # (left, top, width, height)

print('='*30)

# Verifica se a pasta screenshots existe, se não, cria uma nova
if not osPathExists(path):
    osMkdir(path)
    print('Diretório criado com sucesso!')
else:
    print('O diretório já existe.')

# Main loop
num = 1
while True:
    print('='*30)
    print(f'Aguardando {trigger} para printar...')
    keyboardWait(trigger) # Espera a tecla para realizar screenshots

    print(f'Screenshot! --> {num}')
    scr = f'{path}/screenshot ({num:02}).png'
    pagScreenshot(scr, rg)  # Realiza screenshot
    
    num += 1

# Loga no OBS e grava na cena especificada
# OBS deve estar aberto
# A cena e a rede deve ser configurada no app previamente

import obsws_python as obs
import time

HOST, PORT, PASS = '192.168.0.33', 4455, 'JZu542Q1ebpfdpvo'

def main():    
    client = obs.ReqClient(host=HOST, port=PORT, password=PASS)  # conecta
    client.set_current_program_scene('BotScene')                 # coloca cena no ar

    # Inicia gravação
    client.start_record()

    print('Gravando 10 s...')
    time.sleep(10)

    client.stop_record()
    print('Pronto ✔')

if __name__ == '__main__':
    main()

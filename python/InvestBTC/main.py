# Mostra a cotação e os lucros e perdas em BTC

# Necessario configurar [data.txt]
#   'average_price' preço do btc no momento da compra
#   'trade_power'   preço alavancado, se nao for alavancar deixar igual ao 'money'
#   'money'         dinheiro em caixa / valor comprado

import websocket
import json
import os

os.system('TITLE InvestBTC')

#====================================================================================================

global btc_price
btc_price, average_price, trade_power, money = 0,0,0,0

try:
    with open('data.txt', 'x') as file:
        lines = 'average_price=[100000]\ntrade_power=[10000]\nmoney=[1000]\n'
        file.write(lines)
        lines = ['average_price=[100000]\n','trade_power=[10000]\n','money=[1000]\n']

except FileExistsError:
    with open('data.txt', 'r') as file:
        lines = file.readlines()

for line in lines:
    var, dat = line.strip().strip(']').split('=[')
    value = float(dat) if '.' in dat else int(dat)
    globals()[var] = value

#====================================================================================================

def liquidIn():
    l = average_price - (average_price/100*(money*100/trade_power))
    lp = 100 - (l*100/average_price)
    return [l, lp]

def getLong():
    return trade_power/money

def winLost(btc_price):
    x = btc_price*100 / average_price
    wl = ((x * 0.01) * trade_power) - trade_power
    wlp = x - 100
    return [wl, wlp]

#====================================================================================================

def on_message(ws, message):
    os.system('cls')

    data = json.loads(message)
    btc_price = float(data['c'])

    print('='*50)
    print(f'BTC/USDT:          {btc_price:,.2f}\n')

    print(f'Preço medio:       {average_price:,.2f}')
    print(f'Dinheiro em conta: {money:,.2f}')
    print(f'Poder de compra:   {trade_power:,.2f}\n')

    print(f'Alavancado         {getLong():,.2f}x')
    print(f'Liquidado em       {liquidIn()[0]:,.2f}')
    print(f'Liquidado em (%)   -{liquidIn()[1]:,.2f}%\n')

    print(f'Ganhos/Perdas      {winLost(btc_price)[0]:,.2f}')
    print(f'Ganhos/Perdas(%)   {winLost(btc_price)[1]:,.2f}%')
    print('='*50)

def on_error(ws, error):
    print(error) if str(error) != "'c'" else print('Starting...')

def on_close(ws, close_status_code, close_msg):
    print('Conexão fechada')

def on_open(ws):
    # Inscreve no par BTC/USDT
    payload = {
        'method': 'SUBSCRIBE',
        'params': ['btcusdt@ticker'],
        'id': 1
    }
    ws.send(json.dumps(payload))

#====================================================================================================

def main():
    ws = websocket.WebSocketApp('wss://stream.binance.com:9443/ws',
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

main()

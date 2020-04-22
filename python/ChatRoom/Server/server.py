################################################################################

## author: Lucas santos
## version: 1.0
## Python 3.6.5 | UTF-8

import socket
from threading import Thread
from random import randint

################################################################################

class Server:
    def __init__(self, port=4444, channels=5):
        self.port = port
        self.channels = channels

        # Socket configuration
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('', self.port))
        self.server.listen(self.channels)

        print('='*60)
        print('The server is online.')

        # Conection variables
        self.conns = {}
        self.addrs = {}
        self.userIds = []

        # Auxiliary variables
        self.connReceived = None
        self.onlineUsers = 0

        print('Waiting for connections.')
        print('='*60)

        # Thread that accepts connections
        connThread = Thread(target=self.connAccept, daemon=True)
        connThread.start()

        # Function mkLoginThread
        self.mkLoginThread()

    # Accepts connections and saves user data
    def connAccept(self):
        while True:
            conn_addr = self.server.accept()
            userId = self.getUserId()

            self.conns.update( {userId: conn_addr[0]} )
            self.addrs.update( {userId: conn_addr[1]} )

            self.connReceived = userId

    # Create a thread for each user to login them
    def mkLoginThread(self):
        while True:
            if self.connReceived != None:
                Thread(target=self.LoginRecvSend, args=(self.connReceived,),
                       daemon=True).start()

                self.connReceived = None

    # Get an userId that's not in self.userIds
    def getUserId(self):
        while True:
            userId = randint(0, 9999999999)
            if userId not in self.userIds:
                self.userIds.append(userId)
                break
        return userId

    # Receives nicknames and sends messages to all users
    def LoginRecvSend(self, userId):
        try:
            nickname = self.conns[userId].recv(4096).decode('utf8')
        except:
            nickname = None
        else:
            self.msgConnect(nickname, userId)
            self.onlineUsers += 1

        while True:
            try:
                msg = self.conns[userId].recv(4096).decode('utf8')
                self.sendMsgToAll(userId, msg)
                print(msg)

            except:
                self.msgDisconnect(nickname, userId)
                self.userRemove(userId)
                break

    # Send message to all connected users
    def sendMsgToAll(self, userId, msg):
        for userid in self.conns:
            if userid != userId:
                try:
                    self.conns[userid].send(msg.encode('utf8'))
                except:
                    pass

    # Sends to everyone that someone has connected
    def msgConnect(self, nickname, userId):
        print('{} joined the server.'.format(nickname))
        self.sendMsgToAll(userId, '{} joined the server.'.format(nickname))

    # Sends to everyone that someone has disconnected
    def msgDisconnect(self, nickname, userId):
        if nickname != None:
            print('{} disconnected.'.format(nickname))
            self.sendMsgToAll(userId, '{} Disconnected.'.format(nickname))

    # Remove userdata
    def userRemove(self, userId):
        self.conns.pop(userId)
        self.addrs.pop(userId)
        self.userIds.remove(userId)
        self.onlineUsers -= 1

################################################################################

def main():
    Server()

main()

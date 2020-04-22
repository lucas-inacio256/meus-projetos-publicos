################################################################################

## author: Lucas santos
## version: 1.0
## Python 3.6.5 | UTF-8

from tkinter import *
import socket
from threading import Thread
from random import randint
from time import sleep

################################################################################

# Global variables
nickname = 'User' + str(randint(10000, 99999))

################################################################################

class Login(LabelFrame):
    def __init__(self, master, appName):
        super().__init__(master)

        # Tk configuration
        self.master = master
        self.master.geometry('500x400')
        self.master.resizable(height=False, width=False)
        self.master['bg'] = '#252525'

        # LabelFrame configuration
        self.appName = appName
        self.config(text=self.appName, width=450, height=370,
                    padx=15, pady=15)
        self.pack_propagate(False)
        self['fg'] = '#999999'
        self['bg'] = '#252525'

        # Welcome label
        welcomeLabel = Label(self, text='Welcome!',
                             font=('Lucida Grande', 44),
                             fg='#999999', bg='#252525')
        welcomeLabel.pack(pady=50)

        # Nickname label
        nicknameLabel = Label(self, text='Nickname:',
                              fg='#999999', bg='#252525')
        nicknameLabel.pack()

        # Nickname entry
        self.nicknameEntry = Entry(self, fg='#999999', bg='#353535')
        self.nicknameEntry.pack()

        # Login button
        loginButton = Button(self, text='Login', command=self.getNickname,
                             width=16, height=1,
                             fg='#999999', bg='#353535', bd=3)
        loginButton.pack()

        # Warning label
        self.warningLabel = Label(self, fg='#999999', bg='#252525')
        self.warningLabel.pack(pady=30)

        # LabelFrame pack
        self.pack(padx=8, pady=8)

    # Geting user nickname from entry
    def getNickname(self):
        global nickname
        message = self.nicknameEntry.get()

        if message == '':
            self.warningLabel['text'] = 'Please, choose your nickname.'
        elif len(message) < 4:
            self.warningLabel['text'] = 'Too small nickname.'
        elif len(message) > 20:
            self.warningLabel['text'] = 'Too long nickname.'
        else:
            nickname = message
            self.master.destroy()

################################################################################

class ChatRoom(LabelFrame):
    def __init__(self, master, appName, nickname, serverIp, serverPort):
        super().__init__(master)

        # User nickname
        self.nickname = nickname

        # Server configuration
        self.connected = False
        self.serverIp = serverIp
        self.serverPort = serverPort
        self.server = None

        # Tk configuration
        self.master = master
        self.master.geometry('800x550')
        self.master.resizable(height=False, width=False)
        self.master['bg'] = '#252525'

        # LabelFrame configuration
        self.appName = appName
        self.config(text=self.appName)
        self['fg'] = '#999999'
        self['bg'] = '#252525'

        # Chat
        self.chatText = Text(self, width=95, height=27,
                             fg='#999999', bg='#454545',
                             bd=3, state=DISABLED)
        self.chatText.pack(padx=5, pady=5, fill=BOTH, expand=1)
        self.chatText.pack_propagate(False)

        # Scrollbar
        scrollBar = Scrollbar(self.chatText, command=self.chatText.yview)
        scrollBar.pack(side='right', fill=Y)

        self.chatText.config(yscrollcommand=scrollBar.set)

        # Text box
        self.textBox = Text(self, width=83, height=3,
                            fg='#999999', bg='#353535', bd=3)
        self.textBox.pack(side='left', padx=5, pady=5)

        # Enter button
        enterButton = Button(self, text='ENTER', command=self.onEnter,
                             width=10, height=3,
                             fg='#999999', bg='#353535', bd=3)
        enterButton.pack(side='right', padx=5, pady=5)

        # LabelFrame pack
        self.pack(padx=8, pady=8)

        # Thread serverConnect
        Thread(target=self.serverConnect, daemon=True).start()

    # Insert message in chat
    def chatInsert(self, message):
        self.chatText['state'] = NORMAL
        self.chatText.insert(INSERT, message)
        self.chatText['state'] = DISABLED

        self.chatText.see('end')

    # Send message on press ENTER button
    def onEnter(self):
        message = self.textBox.get('1.0', END)
        self.textBox.delete('1.0', END)

        message = '{}: {}'.format(self.nickname, message)
        self.chatInsert(message)

        if self.connected:
            self.server.send(message.replace('\n','').encode('utf8'))

    # Connect to the server and receive messages
    def serverConnect(self):
        self.chatInsert('='*95 + '\n')
        self.chatInsert('Welcome {}!\n'.format(self.nickname))
        self.chatInsert('Trying to connect to the server.\n')

        while True:
            self.connectLoop()
            self.chatInsert('Connected!\n')
            self.chatInsert('='*95 + '\n')
            sleep(1)

            try:
                self.server.send(self.nickname.encode('utf8'))
            except:
                self.chatInsert('='*95 + '\n')
                self.chatInsert('Connection lost.\n')
                self.connected = False

            while self.connected:
                try:
                    msg = self.server.recv(4096).decode('utf8')
                    self.chatInsert(msg + '\n')
                except:
                    self.chatInsert('='*95 + '\n')
                    self.chatInsert('Connection lost.\n')
                    self.connected = False

    def connectLoop(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                self.server.connect((self.serverIp, self.serverPort))
                self.connected = True
                break
            except:
                self.chatInsert('Error when trying to connect to the server.\n')
                sleep(1)

################################################################################

def main():
    loginname = '+Login+'
    chatname = '+ChatRoom+'

    # If you want to use a PUBLIC IP, you need to configure your network.
    SERVER_IP = '' # Paste your ip here
    SERVER_PORT = 4444

    login = Tk(className=loginname)
    loginapp = Login(login, loginname)
    loginapp.mainloop()

    chatroom = Tk(className=chatname)
    chatapp = ChatRoom(chatroom, chatname, nickname, SERVER_IP, SERVER_PORT)
    chatapp.mainloop()

main()

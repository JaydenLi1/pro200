import socket
from threading import Thread
nickname = input("Name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '192.168.1.20'
port = 8000
client.connect((ip_address, port))


def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == "NICKNAME":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("oopise woopise there's a big error bye bye")
            client.close()
            break


def write():
    while True:
        message = '{}:{}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))


receive_thread = Thread(target=receive)
receive_thread.start()

write_thread = Thread(target=write)
write_thread.start()

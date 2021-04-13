import socket
import cryptocode
def client():
    host = "127.0.0.1"
    port = 5001
    c = socket.socket()
    c.connect((host, port))
    message = input("Input:: ")
    while message.lower().strip() != 'end':
        message = cryptocode.encrypt(message, "mysecret")
        c.send(message.encode())
        data = c.recv(1024).decode()
        data = cryptocode.decrypt(message, "mysecret")
        print('Server message: ' + data)
        message = input(" >")
    c.close()
if __name__ == '__main__':
    client()
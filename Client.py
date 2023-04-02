import socket
import threading
import socketserver
 
def client(ip, port, message):
    '''模拟客户端收发消息'''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))
 
if __name__ == "__main__":
        HOST, PORT = "localhost", 9999
        ip, port = HOST, PORT
        client(ip, port, "Hello World 1")
        client(ip, port, "Hello World 2")
        client(ip, port, "Hello World 3")
 
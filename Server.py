# coding=utf-8
# 多线程TCP服务器
 
import socket
import threading
 
bind_ip = "127.0.0.1"  # 监听的IP 地址
bind_port = 9999  # 监听的端口
 
# 建立一个socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# 绑定监听的地址，创建的对象是AF_INET的形式，所以地址(ip, port)的元组形式来表示
server.bind((bind_ip, bind_port))
 
# 启动监听并设置连接数为5
server.listen(5)
 
print("[*] Listening on %s:%d" % (bind_ip, bind_port))
 
 
# 这是客户处理线程，也是一个回调函数，创建一个新的进程对象，将客户端套接字对象作为一个句柄传递给它。
def handle_client(client_socket):
    # 打印处客户端发送得到的内容
    request = client_socket.recv(1024)
 
    print("[*] Received: %s " % request)
 
    # 返还一个 ACK 在计算机网络中的意思是返回包确认，表示收到
    client_socket.send("ACK!".encode())
    client_socket.close()
 
 
# 等待连接,这里必定进入循环
while True:
    # 一个客户端成功建立连接的时候，我们将收到的客户端套接字对象保存到client变量中，将远程连接的细节保存到addr变量中。
    # 返回的client是一个套接字，是表示专属客户的一个新的套接字  |  而addr则是一个tuple元组，抓了某次数据返回的就是('127.0.0.1', 62549)
    # 运行到下面就被当作套接字传递给上面自定义的 handle_client 函数
    client, addr = server.accept()
 
    # 打印结果 在('127.0.0.1', 62549)中addr[0] -> 127.0.0.1，addr[1] -> 62549
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
 
    # 挂起客户端线程，处理传入的数据。
    # Thread是一个类，创建一个新的线程对象，target指定调用的函数，args指定调用函数的参数，是一个元组，后面要加一个’,’
    # 当调用start函数时，就回去执行这个函数
    client_handler = threading.Thread(target=handle_client, args=(client,))
 
    # 启动线程开始处理客户端连接。handle_client 函数执行recv()函数之后将一段信息发送给客户端
    client_handler.start()
import streamlit as st
import socket

page = st.sidebar.radio("我的主页", ["主页"])

# 创建一个socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# 获取本地机器上的IP和端口
host = '127.0.0.1'
port = 2655
 
# 绑定socket到端口
server_socket.bind((host, port))
 
# 设置最大连接数，等待连接的客户端数量
server_socket.listen(1)
 
print(f"Server is listening on {host}:{port}...")
 
# 接受一个新的连接
client_socket, addr = server_socket.accept()
 
print(f"Connected to client {addr[0]}:{addr[1]}")
 
# 接收数据
received_data = client_socket.recv(1024)
print("Received data:", received_data.decode())
 
# 关闭socket连接
client_socket.close()
server_socket.close()

def page1():
    if st.button("跳转"):
        st.write(received_data)
import socket
import threading

# �������� ������
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ��������� ������ � ����� �������
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# ������� ��� �������� ��������� �������
def send_message():
    while True:
        message = input("Enter a message: \n")
        client_socket.sendall(message.encode('utf-8'))

# ������� ��� ��������� ��������� �� �������
def receive_message():
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(f'\nMessage received: {message}')
        print("Enter a message: ")

# ������ ������� ��� �������� � ��������� ���������
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)
send_thread.start()
receive_thread.start()
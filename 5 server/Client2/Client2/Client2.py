import socket
import threading

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Установка адреса и порта сервера
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Функция для отправки сообщений серверу
def send_message():
    while True:
        message = input("Enter a message: \n")
        client_socket.sendall(message.encode('utf-8'))

# Функция для получения сообщений от сервера
def receive_message():
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(f'\nMessage received: {message}')
        print("Enter a message: ")

# Запуск потоков для отправки и получения сообщений
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)
send_thread.start()
receive_thread.start()
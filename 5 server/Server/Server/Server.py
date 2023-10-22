import socket
import threading

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Установка адреса и порта сервера
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Ожидание подключения клиентов
server_socket.listen(2)
print('The server is running and waiting for clients to connect...')

# Список клиентов
clients = []

# Функция для обработки сообщений от клиентов
def handle_client(client_socket, client_address):
    while True:
        try:
            # Получение сообщения от клиента
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f'Message from {client_address}: {message}')
                # Отправка сообщения всем клиентам, кроме отправляющего
                for client in clients:
                    if client != client_socket:
                        client.sendall(message.encode('utf-8'))
            else:
                # Удаление клиента из списка при отключении
                clients.remove(client_socket)
                print(f'Client {client_address} disconnected')
                break
        except:
            # Удаление клиента из списка при ошибке
            clients.remove(client_socket)
            print(f'Client {client_address} disconnected')
            break

# Основной цикл для принятия подключений
while True:
    # Принятие подключения клиента
    client_socket, client_address = server_socket.accept()
    print(f'Client {client_address} connected')

    # Добавление клиента в список
    clients.append(client_socket)

    # Запуск потока для обработки сообщений от клиента
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
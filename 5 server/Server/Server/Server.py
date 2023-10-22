import socket
import threading

# �������� ������
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ��������� ������ � ����� �������
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# �������� ����������� ��������
server_socket.listen(2)
print('The server is running and waiting for clients to connect...')

# ������ ��������
clients = []

# ������� ��� ��������� ��������� �� ��������
def handle_client(client_socket, client_address):
    while True:
        try:
            # ��������� ��������� �� �������
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f'Message from {client_address}: {message}')
                # �������� ��������� ���� ��������, ����� �������������
                for client in clients:
                    if client != client_socket:
                        client.sendall(message.encode('utf-8'))
            else:
                # �������� ������� �� ������ ��� ����������
                clients.remove(client_socket)
                print(f'Client {client_address} disconnected')
                break
        except:
            # �������� ������� �� ������ ��� ������
            clients.remove(client_socket)
            print(f'Client {client_address} disconnected')
            break

# �������� ���� ��� �������� �����������
while True:
    # �������� ����������� �������
    client_socket, client_address = server_socket.accept()
    print(f'Client {client_address} connected')

    # ���������� ������� � ������
    clients.append(client_socket)

    # ������ ������ ��� ��������� ��������� �� �������
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
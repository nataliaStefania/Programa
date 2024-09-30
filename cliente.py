import socket

def start_client():
    # Crear socket de cliente TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor
    server_address = ('localhost', 65432)
    client_socket.connect(server_address)
    print(f"Conectado al servidor {server_address[0]}:{server_address[1]}")

    try:
        # Solicitar al usuario que ingrese las credenciales
        username = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        # Enviar las credenciales al servidor (separadas por una coma)
        credentials = f"{username},{password}"
        client_socket.sendall(credentials.encode('utf-8'))

        # Recibir respuesta del servidor
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Respuesta del servidor: {response}")

    finally:
        # Cerrar la conexión
        client_socket.close()

if __name__ == '__main__':
    start_client()

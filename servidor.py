import socket

# Lista de usuarios y contraseñas
users_db = {
    "natalia": "123",
}

def start_server():
    # Crear el socket del servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Asignar dirección y puerto
    server_address = ('localhost', 65432)
    server_socket.bind(server_address)

    # Escuchar conexiones entrantes
    server_socket.listen(5)
    print(f"Servidor de autenticación iniciado en {server_address[0]}:{server_address[1]} esperando conexiones...")

    while True:
        # Aceptar una conexión de un cliente
        client_socket, client_address = server_socket.accept()
        print(f"Conexión establecida con {client_address}")

        # Recibir nombre de usuario y contraseña
        credentials = client_socket.recv(1024).decode('utf-8')
        username, password = credentials.split(',')

        # Verificar si el nombre de usuario y la contraseña son correctos
        if username in users_db and users_db[username] == password:
            response = "Inicio de sesión exitoso"
        else:
            response = "Credenciales incorrectas"

        # Enviar respuesta al cliente
        client_socket.sendall(response.encode('utf-8'))

        # Cerrar la conexión con el cliente
        client_socket.close()

if __name__ == '__main__':
    start_server()
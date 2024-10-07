from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def send_credentials(username, password):
    # Crear socket de cliente TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 65432)
    client_socket.connect(server_address)

    try:
        # Enviar las credenciales al servidor (separadas por una coma)
        credentials = f"{username},{password}"
        client_socket.sendall(credentials.encode('utf-8'))

        # Recibir respuesta del servidor
        response = client_socket.recv(1024).decode('utf-8')
        return response

    finally:
        client_socket.close()

@app.route('/')
def home():
    return render_template('index.html', message=None)  # Inicialmente sin mensaje

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    response = send_credentials(username, password)

    # Retorna la página principal con el mensaje de respuesta
    return render_template('index.html', message=response)

if __name__ == '__main__':
    app.run(debug=True)
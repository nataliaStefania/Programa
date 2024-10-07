document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar que el formulario se envíe de manera tradicional

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Validar entradas
    if (!username || !password) {
        mostrarMensaje("Por favor, completa ambos campos.", "error");
        return;
    }

    // Enviar las credenciales al servidor Flask
    fetch('/login', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json' 
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        mostrarMensaje(data.message, data.status);
    })
    .catch(error => {
        console.error('Error:', error);
        mostrarMensaje("Ocurrió un error al comunicarse con el servidor.", "error");
    });
});

function mostrarMensaje(mensaje, tipo) {
    const mensajeDiv = document.getElementById('responseMessage');
    mensajeDiv.textContent = mensaje;
    mensajeDiv.style.color = tipo === "success" ? "green" : "red";
}

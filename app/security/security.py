import hashlib

def hash_password(password: str) -> str:
    # Convertimos la contraseña en bytes y generamos el hash sha256
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def check_password(password: str, hashed: str) -> bool:
    # Calculamos el hash de la contraseña proporcionada y lo comparamos con el hash almacenado
    return hash_password(password) == hashed

if __name__ == "__main__":
    hashed_password = hash_password("mi_contraseña_secreta")
    print("Contraseña hash:", hashed_password)

    # Verificación
    es_valida = check_password("mi_contraseña_secreta", hashed_password)
    print("¿Es válida?", es_valida)

    es_valida = check_password("mi_otra_constraseña_secreta", hashed_password)
    print("¿Es válida?", es_valida)



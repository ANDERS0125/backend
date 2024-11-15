from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def check_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

if __name__ == "__main__":
    hashed_password = hash_password("mi_contraseña_secreta")
    print("Contraseña hash:", hashed_password)

    # Verificación
    es_valida = check_password("mi_contraseña_secreta", hashed_password)
    print("¿Es válida?", es_valida)

    es_valida = check_password("mi_otra_constraseña_secreta", hashed_password)
    print("¿Es válida?", es_valida)



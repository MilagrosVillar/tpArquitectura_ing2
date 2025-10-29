
def validar_email(email):
    return "@" in email and "." in email

def validar_texto(texto):
    return len(texto.strip()) > 0
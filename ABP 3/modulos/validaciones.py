def validar_edad(edad):
    try:
        edad = int(edad)
        if edad > 0:
            return edad
        return None
    except:
        return None
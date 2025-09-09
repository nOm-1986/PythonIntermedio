from ..models.usuario import Usuario


def menu(opcion: int):
  if (opcion >= 6 and opcion <= 0):
    return "Ingrese una opción válida"

  if opcion == 1:
    pass

  if opcion == 2:
    return "Seleccionó la opción 2"

  if opcion == 3:
    return "Seleccionó la opción 3"

  if opcion == 4:
    return "Seleccionó la opción 4"

  if opcion == 5:
    return 5

import time

from proyect.app.menu import menu
from proyect.services.utils import greetings_options

if __name__ == "__main__":
  running = True
  print(greetings_options())
  while running:
    try:
      option_selected = int(input("Seleccione una opción para iniciar: "))
      result = menu(option_selected)
      if result == 5:
        print("Gracias por utilizar nuestro SIGT")
        break
    except ValueError as e:
      print(f"{e}")



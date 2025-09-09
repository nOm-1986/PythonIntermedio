from proyect.app.menu import menu

if __name__ == "__main__":
  running = True
  menu()
  while running:
    option_selected = int(input("Seleccione una opción para iniciar: "))
    if option_selected == 7:
      break
  print("Gracias por utilizar nuestro SIGT")
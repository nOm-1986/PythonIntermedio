# RETURN
# Tiene 2 variantes diferentes

# == Return == Cuando se invoca sin ningun argumento solo termina la función.
def feliz_ano(wishes=True):
  print('Tres..')
  print('Dos..')
  print('Uno..')
  if not wishes:
    return
  print("Feliz anoo carajo")

# None === Solo existes 2 circustancias donde None se puede usar de forma segura.
value = None
if value is None:
  print('Lo siento, no contienes ningún valor')

# si una función no devuelve u valor utilizando una claúsula de expresión return
# se asume que es None

def funcion_con_none(numero):
  if numero > 10:
    return 'Es mayor'

print(funcion_con_none(20)) # Es mayor
print(funcion_con_none(2)) # None

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
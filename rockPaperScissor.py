from cgi import print_arguments
from msilib.schema import Condition
import random
from os import system, name

hands = [
""" 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""  
    _______
---'   ____)_____
           ______)
          _______)
         _______)
---.__________)
""",
""" 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

options = ['piedra', 'papel', 'tijera']
computer_wins = 0
user_wins = 0
rounds = 1

def clearConsole():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def choose_options():
    user_option = int(input('Seleccione una opción 1-Piedra, 2-Papel, 3-Tijera: '))
    computer_option = random.choice(options)
    assert user_option != int, "Solo se permiten los números 1, 2 o 3"
    if user_option > 3 or user_option < 1:
        print('Esa opción no es válida')

        condition = True
        while condition:
            user_option = int(input('Seleccione una opción 1-Piedra, 2-Papel, 3-Tijera: '))
            if user_option < 4 and user_option >= 1:
                condition = False
    user_option = options[user_option - 1];
    clearConsole()
    return user_option, computer_option


while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    user_option, computer_option = choose_options()
    rounds += 1

    #print(f'Usted eligió: {options[user_option-1]} - la computadora eligió: {computer_option}')

    if ((user_option == 'piedra' and computer_option == 'tijera') or (user_option == 'papel' and computer_option == 'piedra') or (user_option == 'tijera' and computer_option == 'papel')):
        print(f"Usted eligió: {user_option} - la computador eligió: {computer_option}")
        print('Usted ganó!')
    elif(user_option == computer_option):
        print(f"Usted eligió: {user_option} - la computador eligió: {computer_option}")
        print('Empate')
    else:
        print(f"Usted eligió: {user_option} - la computador eligió: {computer_option}")
        print('Usted perdió')
    
    # if options[user_option-1] == computer_option:
    #     print('Empate')
    # #elif user_option == 'piedra':
    # elif user_option == 1:
    #     if computer_option == 'tijera':
    #         print('piedra gana a tijera')
    #         print('Usted ganó!')
    #     else:
    #         print('papel gana a piedra')
    #         print('Usted perdió!')
    # #elif user_option == 'papel':
    # elif user_option == 2:
    #     if computer_option == 'piedra':
    #         print('papel gana a piedra')
    #         print('Usted ganó!')
    #     else:
    #         print('tijera gana a papel')
    #         print('Usted perdió!')
    # #elif user_option == 'tijera':
    # elif user_option == 3:
    #     if computer_option == 'papel':
    #         print('tijera gana a papel')
    #         print('Usted ganó!')
    #     else:
    #         print('piedra gana a tijera')
    #         print('Usted perdió!')

    if rounds == 5:
        break




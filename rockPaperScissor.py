import random


user_option = int(input('Seleccione una opción 1-Piedra, 2-Papel, 3-Tijera: '))
options = ['piedra', 'papel', 'tijera']
computer_option = random.choice(options)

if user_option > 3 or user_option < 1:
    print('Esa opción no es válida')

else:
    print(f'Usted eligió: {options[user_option-1]} - la computadora eligió: {computer_option}')
    if options[user_option-1] == computer_option:
        print('Empate')
    #elif user_option == 'piedra':
    elif user_option == 1:
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('Usted ganó!')
        else:
            print('papel gana a piedra')
            print('Usted perdió!')
    #elif user_option == 'papel':
    elif user_option == 2:
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('Usted ganó!')
        else:
            print('tijera gana a papel')
            print('Usted perdió!')
    #elif user_option == 'tijera':
    elif user_option == 3:
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('Usted ganó!')
        else:
            print('piedra gana a tijera')
            print('Usted perdió!')

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

print(hands[2])



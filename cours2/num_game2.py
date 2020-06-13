import sys
from random import randint

num = randint(1, 10)
tries = 3
user_num = None # Donne une valeur pour vérifier la condition de la boucle while avant de demander l'input de l'user

print('J\'ai choisi un nombre compris entre 1 et 10. Essaie de le deviner !')

# Jeu avec 3 chances
while tries > 0 and user_num != num:
    print('Chance(s) restante(s) ' + str(tries))
    try:
        user_input = int(input('Donne un nombre entre 1 et 10 : ' ))
    except ValueError as error:
        print("NON " + str(error))
        sys.exit(1)
    if user_num == num:
        print('Bien joué ! Tu as trouvé !')
    elif user_num < num:
        print('Trop bas...')
    else:
        print('Trop haut...')
    tries -= 1

if user_num != num:
    print('Dommage ! La réponse était : ' + str(num) + '.')
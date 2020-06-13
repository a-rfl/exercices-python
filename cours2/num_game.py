from random import randint

num = randint(1, 10)

# 1ère chance
user_num = int(input('J\'ai choisi un nombre compris entre 1 et 10. Essaie de le deviner ! ' ))

if user_num == num:
    print('Bien joué tu as trouvé !')
elif user_num < num:
    print('Trop bas...')
        # Trop petit :  2ème chance
    user_num = int(input('Réessaie ! ' ))
    if user_num == num:
        print('Bien joué tu as trouvé !')
    elif user_num < num:
        print('Trop bas...')
        # Trop petit - trop petit : 3ème chance
        user_num = int(input('Réessaie ! ' ))
        if user_num == num:
            print('Bien joué tu as trouvé !')
        elif user_num < num:
            print('Trop bas... La réponse était : ' + str(num))
        else:
            print('Trop haut... La réponse était : ' + str(num))
    else:
        print('Trop haut...')
        # Trop petit - trop grand : 3ème chance
        user_num = int(input('Réessaie ! ' ))
        if user_num == num:
            print('Bien joué tu as trouvé !')
        elif user_num < num:
            print('Trop bas... La réponse était : ' + str(num))
        else:
            print('Trop haut... La réponse était : ' + str(num))
else:
    print('Trop haut...')
    # Trop grand : 2ème chance
    user_num = int(input('Réessaie ! ' ))
    if user_num == num:
        print('Bien joué tu as trouvé !')
    elif user_num < num:
        print('Trop bas...')
        # Trop grand - trop petit : 3ème chance
        user_num = int(input('Réessaie ! ' ))
        if user_num == num:
            print('Bien joué tu as trouvé !')
        elif user_num < num:
            print('Trop bas... La réponse était : ' + str(num))
        else:
            print('Trop haut... La réponse était : ' + str(num))
    else:
        print('Trop haut...')
        # Trop grand - trop grand :3ème chance
        user_num = int(input('Réessaie ! ' ))
        if user_num == num:
            print('Bien joué tu as trouvé !')
        elif user_num < num:
            print('Trop bas... La réponse était : ' + str(num))
        else:
            print('Trop haut... La réponse était : ' + str(num))

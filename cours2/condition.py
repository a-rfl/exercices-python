import sys
#Convertion de l'input en nombre entier

class MonErreur(Exception):
    pass

user_age = None
while user_age is None:
    try:
        if len(sys.argv) >= 2:
            user_age = int(sys.argv[1])
        else:
            user_age = int(input("Quel âge avez-vous ? "))
    except ValueError:
        print("Pas bon")
    except KeyboardInterrupt:
        print("Stop quitter de force!")

if user_age < 18:
    print('Désolée, vous êtes trop jeune.')
elif user_age > 130:
    print('Désolée, vous être trop âgé.')
else:
    print('Bienvenue à Interface3 !')

print('--FIN--')
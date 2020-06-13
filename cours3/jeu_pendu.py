from random import choice

words = ["emilie", "marine", "laetitia", "katarina", "bastien", "alice", "aurelie"]

# Sélectionne le mot à deviner dans la liste selon l'index trouvé
word_to_find = choice(words)
word_to_find = list(word_to_find)
# Crée une str contenant autant de '-' que de lettre dans le mot à deviner 
hidden_word = "-" * len(word_to_find)
hidden_word = list(hidden_word)

# Crée une liste vide où viendra s'ajouter les propositions de l'user
list_prop = []

while len(list_prop) < 10:
    print("Essai(s) : " + "/".join(list_prop))
    user_prop = input("Entrer une lettre minuscule: ")
    list_prop.append(user_prop)
    # Initialisation de l'index
    index = 0
    # Tant que l'index est diff. de la longueur de liste word_to_wind
    while index != len(word_to_find):
        # Si user_prop est identique à l'él. de liste word_to_find à l'index courant
        if user_prop == word_to_find[index]:
            # Alors il vérifie si l'él. de hidden_word à l'index courant est identique à la str "-"
            if hidden_word[index] == "-" :
                # Alors il enlève l'él. de la liste hidden_word (à l'index courant)
                hidden_word.pop(index)
                # La remplace par la valeur de de user_prop
                hidden_word.insert(index, user_prop)
                # Affiche hidden_word en la transformant en str à l'aide de .join()
                print("".join(hidden_word))
        # Incrémente l'index de 1
        index += 1
        
# Si hidden_word est identique à word_to_find
if hidden_word == word_to_find:
    # Alors il affiche "Bravo ! Vous avez trouvé !"
    print("Bravo ! Vous avez trouvé !")
    # Sinon il affiche "Perdu ! Le mot était:" avec word_to_find transformé en str
else:
    print("Perdu ! Le mot était: " + "".join(word_to_find))
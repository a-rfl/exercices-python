# version 1
# le for passe en revu chaque lettre du mot à deviner et la place dans la var element
for element in word_to_find:
    for place in range(0, len(word_to_find) - 1):
        # le if vérifie si la prop. de l'user est identique à la lettre du mot à deviner couramment dans la var element
        if user_prop == element:
                if hidden_word[place] == "-" :
                    hidden_word.pop(place)
                    hidden_word.insert(place, user_prop)
                    print(hidden_word)    
                else: 
                    place += 1
                    print(list_prop)
        
                user_prop = input("Entrer une lettre minuscule: ")
                list_prop.append(user_prop)
# version 2 
while hidden_word != word_to_find:
    index = 0
    if user_prop == word_to_find[index]:
        if hidden_word[index] == "-" :
            hidden_word.pop(index)
            hidden_word.insert(index, user_prop)
            print(hidden_word)
    else: 
        index += 1
        print(list_prop)

    user_prop = input("Entrer une lettre minuscule: ")
    list_prop.append(user_prop

# version 3
while hidden_word != word_to_find:
    index = 0
    if user_prop == word_to_find[index]:
        if hidden_word[index] == "-" :
            hidden_word.pop(index)
            hidden_word.insert(index, user_prop)
            print(hidden_word)
        else:
            index += 1
    else: 
        user_prop = input("Entrer une lettre minuscule: ")
        list_prop.append(user_prop)

# version 4
index = 0
while hidden_word != word_to_find:
    if user_prop == word_to_find[index]:
        for element in hidden_word:
            if hidden_word[index] == "-" :
                hidden_word.pop(index)
                hidden_word.insert(index, user_prop)
                print(hidden_word)
    else: 
        user_prop = input("Entrer une lettre minuscule: ")
        list_prop.append(user_prop)
    index += 1

# version 5
index = 0
while hidden_word != word_to_find:
    user_prop = input("Entrer une lettre minuscule: ")
    if user_prop == word_to_find[index]:
        for element in hidden_word:
            if element == "-" :
                hidden_word.pop(index)
                hidden_word.insert(index, user_prop)
                print(hidden_word)
                index += 1
    else: 
        user_prop = input("Entrer une lettre minuscule: ")
        list_prop.append(user_prop)

# version 6 
index = 0
while hidden_word != word_to_find:
    user_prop = input("Entrer une lettre minuscule: ")
    for element in hidden_word:
        if user_prop == word_to_find[index]:
            if hidden_word[index] == "-" :
                hidden_word.pop(index)
                hidden_word.insert(index, user_prop)
                print(hidden_word)
                index += 1
        else: 
            user_prop = input("Entrer une lettre minuscule: ")
            list_prop.append(user_prop)

# version 7
while hidden_word != word_to_find:
    user_prop = input("Entrer une lettre minuscule: ")
    list_prop.append(user_prop)
    for element in word_to_find:
        index = word_to_find.index(element)
        if user_prop == element:
            if hidden_word[index] == "-" :
                hidden_word.pop(index)
                hidden_word.insert(index, user_prop)
                print("".join(hidden_word))

print("Bravo ! Vous avez trouvé !")

# version 8
while hidden_word != word_to_find:
    print("Essai(s) : " + "/".join(list_prop))
    user_prop = input("Entrer une lettre minuscule: ")
    list_prop.append(user_prop)
    index = 0
    while index != len(word_to_find):
        if user_prop == word_to_find[index]:
            if hidden_word[index] == "-" :
                hidden_word.pop(index)
                hidden_word.insert(index, user_prop)
                print("".join(hidden_word))
        index += 1
print("Bravo ! Vous avez trouvé !")

# version 9
while len(list_prop) < 10:
    print("Essai(s) : " + "/".join(list_prop))
    user_prop = input("Entrer une lettre minuscule: ")
    list_prop.append(user_prop)
    index = 0
    while index != len(word_to_find):
        if user_prop == word_to_find[index]:
            if hidden_word[index] == "-" :
                hidden_word.pop(index)
                hidden_word.insert(index, user_prop)
                print("".join(hidden_word))
        index += 1
if hidden_word == word_to_find:
    print("Bravo ! Vous avez trouvé !")
else:
    print("Perdu ! Le mot était: " + "".join(word_to_find))

# version prof
while hidden_word != word_to_find:
    print(hidden_word)
    user_prop = input("Entrer une lettre minuscule: ")
    list_prop.append(user_prop)

    hidden_word = ""
    for element in word_to_find:
        if element in user_prop:
           hidden_word +=  element
        else:
            hidden_word += "-"
print("Bravo ! Le mot était : " + hidden_word)
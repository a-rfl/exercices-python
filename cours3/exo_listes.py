
my_list = ["Python", "Javascript", "PHP", "HTML", "CSS", "C"]

# 1. Afficher l'avant-dernier élément
print("Exercie 1:")
print(my_list[-2])

# 2. Ajouter un 7è élément à la fin de la liste, et afficher la liste complète
print("Exercie 2:")
my_list.append("java")
print(my_list)

# 3. Retirer l'élément à l'index 3 de la liste et le sauver dans une variable, et afficher la liste complète
print("Exercie 3:")
element = my_list.pop(3)
print(my_list)

# 4. Remettre l'élément retiré au point 3. à l'index 1 de la liste, et affichez la liste
print("Exercie 4:")
my_list.insert(1, element)
print(my_list)

# 5. Afficher un élément choisi au hasard dans la liste
print("Exercie 5:")
from random import choice # Avec la méthode choice
print(choice(my_list)) 

from random import randint # Avec la méthode randint
num = randint(0, len(my_list) - 1) # len(my-list) permet de généraliser l'expression pour qu'elle fonction avec autant d'él. que souhaités. Le "-1" permet de donner le nombre d'index maximum de la liste au lieu du nombre d'él. total.
print(my_list[num])

# Bonus. Faire une boucle qui peut retirer les N premiers éléments de la liste, et les remettre à la fin.
# Ex : N = 2, la liste [1, 2, 3, 4] deviendrait [3, 4, 1, 2]
print("Exercie 6:")
counter = 0
while counter < 3:
    el = my_list.pop(0)
    my_list.append(el)
    counter += 1
print(my_list)

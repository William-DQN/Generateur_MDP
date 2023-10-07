#Le but de ce code est de fournir un mot de passe selon un nombre de caractères qu'il peut lui même définir.
import string
import random
#Liste des minuscules
list1 = [chr(i) for i in range(ord('a'), ord('z')+1)]
#Liste des majuscules
list2 = [chr(i) for i in range(ord('A'), ord('Z')+1)]
#Liste des caractères spéciaux
list3 = list(string.punctuation) + [chr(i) for i in range(ord('!'), ord('/')+1)]
#On transforme les int en str pour permettre une concaténation
list4 = [str(i) for i in range(9)]
#Mix de toutes les listes
gigaliste = list1 + list2 + list3 + list4
#On va demander au moins 8 caractères et max 116 caractères afin d'avoir un minimum de sécurité et éviter les bugs 
def gener(nbruser):
    if nbruser < 8 or nbruser > 116:
        return None
    else:
        password = ''.join(random.choice(gigaliste) for _ in range(nbruser))
        return password

nbruser = None
#On boucle jusqu'à ce que l'utilisateur respecte les conditions imposées.
while True:
    try:
        nbruser = int(input("Veuillez entrer un nombre entre 8 et 116 : "))
        password = gener(nbruser)
        if password:
            print("Votre nouveau mot de passe est :"+ password)
            break
        else:
            print("Vous n'avez pas respecté la condition. Il est important d'avoir un mot de passe d'une longueur minimale de 8.")
    except ValueError:
        print("Veuillez entrer un nombre entier.")

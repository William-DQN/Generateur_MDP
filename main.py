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
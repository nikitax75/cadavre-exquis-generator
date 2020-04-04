
# Mon programme va générer aléatoirement des phrases, j'ai donc besoin du module random:

import random

# aller chercher les mots nécessaires dans chaque fichier (2 nouns, 1 verb et 1 adverb), et assigner une variable à chaque élément:
# 1) convertir file en list et prendre un no de la liste au hasard 2) lire une ligne du fichier au hasard, en connaissant la longueur du fichier
def funny_generator (filename):
    fdp = open(filename, "r")
    selected_list = fdp.readlines()
    fdp.close()
    choice = random.choice(selected_list)
    return choice.rstrip()

noun1 = funny_generator("nouns.dict")
verb = funny_generator("verbs.dict")
noun2 = funny_generator("nouns.dict")
adverb = funny_generator("adverbs.dict")
#-*-coding:utf-8-*-
print(noun1 + " "+ verb + " " + noun2 + " " + adverb)






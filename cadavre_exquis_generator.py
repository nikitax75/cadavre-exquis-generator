
import random

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

print(noun1 + " "+ verb + " " + noun2 + " " + adverb)

#Remarks:
# the function name funny_generator: retrieve_word_from_path is a good example
# you have a couple blank lines at the end, try to avoid

#New exercice rules:
# Figure out a way to store and retrieve nouns, adverbs and verbs in only one file words.dict You will have to invent a smart way of storing/isolating nouns adverbs and verbs in the file
# Transform this program into an executable where the word dictionnary becomes a parameter. You will then be able to call your python script externally this way: python cadavre_exqui_generator.py words.dict 2 . Where 2 reperesents the number of sentences to generate. There are numerous exemple to do this on the internet, you will have to use a main function. 
# Please focus on code cleanliness and minimalism.




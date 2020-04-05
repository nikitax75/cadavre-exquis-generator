import random
import json

with open("stupiddict.json","r") as fdpjason:
    jason_arrays = json.load(fdpjason)
    nouns_dict = jason_arrays["nouns"]
    verbs_dict = jason_arrays["verbs"]
    adverbs_dict = jason_arrays["adverbs"]
    noun1 = random.choice(nouns_dict)
    verb = random.choice(verbs_dict)
    noun2 = random.choice(nouns_dict)
    adverb = random.choice(adverbs_dict)
    print (noun1 + " " + verb + " " + noun2 + " " + adverb)

#Remarks:

#New exercice rules:
# Figure out a way to store and retrieve nouns, adverbs and verbs in only one file words.dict You will have to invent a smart way of storing/isolating nouns adverbs and verbs in the file
# Transform this program into an executable where the word dictionnary becomes a parameter. You will then be able to call your python script externally this way: python cadavre_exqui_generator.py words.dict 2 . Where 2 reperesents the number of sentences to generate. There are numerous exemple to do this on the internet, you will have to use a main function. 
# Please focus on code cleanliness and minimalism.
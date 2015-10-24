import os
import re

base = os.path.dirname(os.path.realpath(__file__))
fabbreviations = open(base + "/data/abbreviations.txt", "r")
fbritish = open(base + "/data/british.txt", "r")
fcontractions = open(base + "/data/contractions.txt", "r")
fspellfix = open(base + "/data/spellfix.txt", "r")

def initialize_dict(fil):
    data = {}
    for line in fil.readlines():
        data[line.split()[0].lower().replace("_", " ")] = line.split()[1].replace("+", " ")
    return data

def text_normalization(text, data):
    text_list = text.split()
    return_text = ""
    for word in text_list:
        change = False
        for key, value in data.iteritems():
            if key.lower() == word.lower():
                if word.istitle():
                    return_text += value.title() + " "
                elif word.isupper() and word != "FB":
                    return_text += value.upper() + " "
                else:
                    return_text += value + " "
                change = True
                break
        if not change:
            return_text += word + " "
    return whitespace(return_text).strip()

def whitespace(text):
    text = re.sub('([.,!?()])', r'\1 ', text)
    text = re.sub('\s{2,}', ' ', text)
    return re.sub(r'\s([.,!?()](?:\s|$))', r'\1', text).strip()

def uppercase(matchobj):
    return matchobj.group(0).upper()

def capitalize(text):
    return re.sub('^([a-z])|[\.|\?|\!]\s*([a-z])|\s+([a-z])(?=\.)', uppercase, text).strip()

def spellfix(text):
    return text_normalization(text, spellfix_dict)

def abbreviations(text):
    return text_normalization(text, abbreviations_dict)

def british(text):
    return text_normalization(text, british_dict)

def contractions(text):
    return text_normalization(text, contractions_dict)

def normalize(text):
    return whitespace(capitalize(spellfix(british(contractions(abbreviations(text)))))).strip()

abbreviations_dict = initialize_dict(fabbreviations)
british_dict = initialize_dict(fbritish)
contractions_dict = initialize_dict(fcontractions)
spellfix_dict = initialize_dict(fspellfix)

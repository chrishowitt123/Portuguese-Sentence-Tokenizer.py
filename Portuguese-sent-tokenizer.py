import nltk
import re
import os
nltk.download('machado')
sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')

os.chdir(r'C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\396200521_TM_ON\Orignal')

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

file = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\396200521_TM_ON\Orignal\Relatório e Contas 2020_2370421_VF.txt"
raw_text = open(file, 'r').read()

replace_dict = {'e.g.': 'por exemplo',
                'ex.' : 'por exemplo',
                '* '  : '', 
                '\t'  : '',}

raw_text = replace_all(raw_text, replace_dict)
re.sub(r'\n+',  '. ', raw_text)

sentences = sent_tokenizer.tokenize(raw_text)

for sent in sentences:
    print(sent)
    print('\n')
    
textfile = open("portuguese_sents.txt", "w")
for sent in sentences:
    textfile.write(sent + "\n")
textfile.close()

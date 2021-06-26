import nltk
import re
nltk.download('machado')
sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

file = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\396200521_TM_ON\Orignal\Relatório e Contas 2020_2370421_VF.txt"
raw_text = open(file, 'r').read()

replace_dict = {'e.g.': 'por exemplo',
                'ex.' : 'por exemplo',
                '* '  : '', 
                '\t'  : '',
                '\n'  : '. '}

raw_text = replace_all(raw_text, replace_dict)

sentences = sent_tokenizer.tokenize(raw_text)

for sent in sentences:
    print(sent)
    print('\n')

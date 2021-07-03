import nltk
import re
import docx2txt
import os
nltk.download('machado')
sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')

os.chdir(r'C:\Users\chris\Desktop\Find and replace')

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

file = r"HLA.P.1653_RNT EIA Aquisição Sísmica Offshore Bloco 5-06_Final_20201105.docx"
text = docx2txt.process(file)

replace_dict = {'e.g.': 'por exemplo',
                'ex.' : 'por exemplo',
                'Exmos.' : 'Exmos',
                '* '  : '', 
                '\t'  : '',}

text = replace_all(text, replace_dict)
text = re.sub(r'(\n+)',  '\n', text).replace('..', '.').replace(';.', '.').replace(';.', '.')

sentences = sent_tokenizer.tokenize(text)

for sent in sentences:
    print(sent)
    print('\n')
    
textfile = open(f"SPLITS_{file.replace('.docx', '.txt')}", "w")
for sent in sentences:
    textfile.write(sent + "\n")
textfile.close()

import nltk
import re
import docx2txt
import os
nltk.download('machado')
sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')

os.chdir(r'C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\405010721_TM_NCR\Translation\Python')

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

file = r"ORIGNAL.docx"
text = docx2txt.process(file)

replace_dict = {'e.g.': 'por exemplo',
                'ex.' : 'por exemplo',
                'Exmos.' : 'Exmos',
                '* '  : '', 
                '\t'  : '',
                'Kz.' : 'Kz'}

text = replace_all(text, replace_dict)
text = re.sub(r'(\n+)',  '\n', text).replace('..', '.').replace(';.', '.').replace(';.', '.')

sentences = sent_tokenizer.tokenize(text)
sentences = [s.split('\n') for s in sentences]
sentences = sum(sentences, [])

for sent in sentences:
    print(sent)
    print('\n' * 2)
    
textfile = open(f"SPLITS_{file.replace('.docx', '.txt')}", "w")
for sent in sentences:
    textfile.write(sent + "\n" * 2)
textfile.close()

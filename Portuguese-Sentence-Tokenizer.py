import nltk
import re
import docx2txt
import os
nltk.download('machado')
sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')

"""
A program that cleans and tokenizes Portuguese text.

"""

os.chdir(r'')

# function that uses a dictionary to replaces items within a body of text
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

file = r"ORIGNAL.docx"

# define text object
text = docx2txt.process(file)

# define before and after pairs
replace_dict = {'e.g.': 'por exemplo',
                'ex.' : 'por exemplo',
                'Exmos.' : 'Exmos',
                '* '  : '', 
                '\t'  : '',
                'Kz.' : 'Kz'}

# clean text using function
text = replace_all(text, replace_dict)

# prepare text for splitting into sentences
text = re.sub(r'(\n+)',  '\n', text).replace('..', '.').replace(';.', '.').replace(';.', '.')

# split text into sentences
sentences = sent_tokenizer.tokenize(text)
sentences = [s.split('\n') for s in sentences]
sentences = sum(sentences, [])

# print results
for sent in sentences:
    print(sent)
    print('\n' * 2)
    
textfile = open(f"SPLITS_{file.replace('.docx', '.txt')}", "w")

# write to text file
for sent in sentences:
    textfile.write(sent + "\n" * 2)
textfile.close()

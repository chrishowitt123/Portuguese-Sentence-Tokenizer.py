import nltk
nltk.download('machado')

file = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\396200521_TM_ON\Orignal\Relatório e Contas 2020_2370421_VF.txt"

sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')
raw_text = open(file, 'r').read().replace("e.g.", "por exemplo").replace("ex.", "por exemplo").replace("* ", "")
sentences = sent_tokenizer.tokenize(raw_text)
for sent in sentences:
    print(sent)
    print('\n')

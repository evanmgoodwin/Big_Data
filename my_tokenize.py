import nltk
from nltk import word_tokenize
text = word_tokenize("Cats are the cutest animals in the whole world!")
output = nltk.pos_tag(text)
print(output)
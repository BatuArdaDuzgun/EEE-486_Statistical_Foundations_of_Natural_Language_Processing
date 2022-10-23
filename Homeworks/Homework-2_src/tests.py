import math

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#nltk.download()


text = "this is a great day"
tokens = nltk.word_tokenize(text)

pos_tag_tokens = nltk.pos_tag(tokens, tagset="universal")


a = wordnet.NOUN

L = math.ulp(0.0)

log_L = math.log10(L)

L2 = 10 ** log_L

print("I am happy testting :D")
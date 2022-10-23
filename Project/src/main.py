import nltk
import time

import os
import string
import random as rd

import numpy as np

import custom_lemmatizer
from tabulate import tabulate

from scipy.stats import binom

import math

import gensim.downloader



stop_words = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out",
                "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such",
                "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him",
                "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don",
                "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while",
                "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them",
                "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because",
                "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just",
                "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if",
                "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]

def Preproces(input_text, remove_stopwords):

    # removing the punctuation and apostrophe
    temp_text = input_text.translate(str.maketrans("’", " ", "‘’" + string.punctuation))

    # making it all lower case
    temp_text = temp_text.lower()

    if remove_stopwords:

        text_words = temp_text.split()
        NSW_text_words = [word for word in text_words if word.lower() not in stop_words]
        temp_text = ' '.join(NSW_text_words)

    return temp_text


print('The nltk version is {}.'.format(nltk.__version__))


ham_mails = []
spam_mails = []

ham_path = "ham"
spam_path = "spam"

print("\n\n*** reading the emials into list ***\n")

print("For Enron 1")
folder = "enron1"

start_time = time.time()
ham_adresses = os.listdir(f"{folder}\{ham_path}")
spam_adresses = os.listdir(f"{folder}\{spam_path}")

for address in ham_adresses:
    f = open(f"{folder}\{ham_path}\{address}", 'r', encoding='utf-8', errors='replace')
    ham_mails.append(f.read())
    f.close()

for address in spam_adresses:
    f = open(f"{folder}\{spam_path}\{address}", 'r', encoding='utf-8', errors='replace')
    spam_mails.append(f.read())
    f.close()


print("--- %s seconds taken reading the folder ---" % (time.time() - start_time))


print("\n\n*** Preprocesing the emails ***\n")
start_time = time.time()

for i in range(len(ham_mails)):
    ham_mails[i] = Preproces(ham_mails[i], False)

for i in range(len(spam_mails)):
    spam_mails[i] = Preproces(spam_mails[i], False)

print("--- %s seconds taken preprocessing the mails ---" % (time.time() - start_time))


print("\n\n*** Tokenizing the emails ***\n")
start_time = time.time()

ham_mail_tokens = []
spam_mail_tokens = []

for mail in ham_mails:
    temp_tokens = nltk.word_tokenize(mail)
    ham_mail_tokens.append(temp_tokens)

for mail in spam_mails:
    temp_tokens = nltk.word_tokenize(mail)
    spam_mail_tokens.append(temp_tokens)


print("--- %s seconds taken turning mails into tokens ---" % (time.time() - start_time))



print("\n\n*** creating vector representation of the tokens ***\n")
start_time = time.time()

ham_mail_token_vectors = []
spam_mail_token_vectors = []

# Download the "glove-twitter-50" embeddings
glove_vectors = gensim.downloader.load('glove-twitter-200')

print("--- %s seconds taken initilizing the word2vec ---" % (time.time() - start_time))
start_time = time.time()

for mail_index in range(len(ham_mail_tokens)):
    temp = []
    for token in ham_mail_tokens[mail_index]:
        if token in glove_vectors:
            temp.append(glove_vectors[token])

    ham_mail_token_vectors.append((ham_path, temp))

for mail_index in range(len(spam_mail_tokens)):
    temp = []
    for token in spam_mail_tokens[mail_index]:
        if token in glove_vectors:
            temp.append(glove_vectors[token])

    spam_mail_token_vectors.append((spam_path, temp))

print("--- %s seconds taken turning tokens into vectors ---" % (time.time() - start_time))

mergered_spam_ham_final = ham_mail_token_vectors + spam_mail_token_vectors
#rd.shuffle(mergered_spam_ham_final)

f = open("vector_mails.txt", 'w')

for mail in mergered_spam_ham_final:

    type = mail[0]
    vectors = mail[1]

    f.write(type + " ")

    for word_vector in vectors:
        for number in word_vector:
            f.write(str(number) + " ")

    f.write("\n")

f.close()

print("I am happy")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

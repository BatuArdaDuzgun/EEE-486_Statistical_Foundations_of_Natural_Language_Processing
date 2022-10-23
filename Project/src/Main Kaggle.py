import nltk
import time

import os
import string
import random as rd

import pandas as pd
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

print("Kaggle 1")


start_time = time.time()

df1 = pd.read_csv('SMS_test.csv', engine='python', encoding='ISO-8859-1')
df2 = pd.read_csv('SMS_train.csv', engine='python', encoding='ISO-8859-1')

df = pd.concat([df1, df2], axis=0)

for index, row in df.iterrows():

    if row["Label"] == "Spam":
        spam_mails.append(row["Message_body"])
    else:
        ham_mails.append(row["Message_body"])








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



print("\n\n*** shufling the mails ***\n")

ham_mail_tokens_tagged = []
spam_mail_tokens_tagged = []

for i in ham_mail_tokens:
    ham_mail_tokens_tagged.append(("ham", i))

for i in spam_mail_tokens:
    spam_mail_tokens_tagged.append(("spam", i))

mergered_spam_ham_final = ham_mail_tokens_tagged + spam_mail_tokens_tagged
rd.shuffle(mergered_spam_ham_final)



print("\n\n*** creating text representation of the tokens ***\n")

training_percent = 0.7
validation_percent = 0.8

training = mergered_spam_ham_final[0: math.floor(len(mergered_spam_ham_final)*training_percent)]
vali = mergered_spam_ham_final[math.floor(len(mergered_spam_ham_final)*(training_percent)):math.floor(len(mergered_spam_ham_final)*(validation_percent))]
test = mergered_spam_ham_final[math.floor(len(mergered_spam_ham_final)*(validation_percent)):]

f = open("kg-train-stemmed.txt", 'w', encoding='utf-8', errors='replace')

for mail in training:

    type = mail[0]
    words = mail[1]

    f.write(type + "\t")

    for i in range(len(words)):
        if i < len(words) - 1:
            f.write(words[i] + " ")
        else:
            f.write(words[i] + "\n")


f.close()

f = open("kg-test-stemmed.txt", 'w', encoding='utf-8', errors='replace')

for mail in test:

    type = mail[0]
    words = mail[1]

    f.write(type + "\t")

    for i in range(len(words)):
        if i < len(words) - 1:
            f.write(words[i] + " ")
        else:
            f.write(words[i] + "\n")

f.close()


f = open("kg-dev-stemmed.txt", 'w', encoding='utf-8', errors='replace')

for mail in vali:

    type = mail[0]
    words = mail[1]

    f.write(type + "\t")

    for i in range(len(words)):
        if i < len(words) - 1:
            f.write(words[i] + " ")
        else:
            f.write(words[i] + "\n")

f.close()



print("I am happy")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

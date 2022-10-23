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

start_time = time.time()

mergered_spam_ham_final = []


f = open("vector_mails.txt", 'r')

for mail in f.readlines():

    temp = mail[:-1]
    temp_list = temp.split()

    type = temp_list[0]

    temp_number_of_words_in_mail = (len(temp_list)-1)/200

    temp_word_vectors_of_mail = []

    for i in range(int(temp_number_of_words_in_mail)):

        temp_word_vector = temp_list[(i*200 + 1): (i*200 + 51)]

        temp_word_vectors_of_mail.append(temp_word_vector)


    mergered_spam_ham_final.append((type, np.array(temp_word_vectors_of_mail)))


f.close()

print("--- %s seconds taken to read the procesed data of the file ---" % (time.time() - start_time))












print("I am happy")



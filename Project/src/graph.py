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



f = open("graph.txt", 'r', encoding='utf-8', errors='replace')

text = ""

lines = []

for line in f.readlines():

    text += line
    lines.append(line)

lines = text.split("\n")[:-2]

parts = []

for line in lines:

    parts.append(line.split(","))


training_loss = []
for part in parts:
    training_loss.append(part[1].split(" ")[-1])

training_acc = []
for part in parts:
    training_acc.append(part[2].split("%")[0])


f.close()

print("--- %s seconds taken to read the procesed data of the file ---")
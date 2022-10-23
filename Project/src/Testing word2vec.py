import gensim.downloader

# Download the "glove-twitter-25" embeddings
glove_vectors = gensim.downloader.load('glove-twitter-50')

test = glove_vectors.most_similar('twitter')



print("I am happy")

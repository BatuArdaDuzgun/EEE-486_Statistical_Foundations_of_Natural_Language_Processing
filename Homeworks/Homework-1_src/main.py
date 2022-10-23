import os
import string
import random as rd
import numpy as np
import matplotlib.pyplot as plt

books_path = "books"
PP_books_path = "PP_books"
NSW_PP_books_path = "NSW_PP_books"

authors = "Authors"
genres = "Types"


random_corpus_file_name = "random_corpus.txt"


book_classes = [authors, genres]

writer_names = ["Charles Dickens", "Fyodor Dostoevsky", "Graf Leo Tolstoy"]
genra_names = ["Fantasy", "Horror", "Romance"]

vocabulary_file = {PP_books_path: {authors: {writer_names[0]: [], writer_names[1]: [], writer_names[2]: []},
                                   genres: {genra_names[0]: [], genra_names[1]: [], genra_names[2]: []}},
                   NSW_PP_books_path: {authors: {writer_names[0]: [], writer_names[1]: [], writer_names[2]: []},
                                   genres: {genra_names[0]: [], genra_names[1]: [], genra_names[2]: []}}}

corpus_size_file = {PP_books_path: {authors: {writer_names[0]: [], writer_names[1]: [], writer_names[2]: []},
                                   genres: {genra_names[0]: [], genra_names[1]: [], genra_names[2]: []}},
                   NSW_PP_books_path: {authors: {writer_names[0]: [], writer_names[1]: [], writer_names[2]: []},
                                   genres: {genra_names[0]: [], genra_names[1]: [], genra_names[2]: []}}}

corpus_size_slope_file = {PP_books_path: {authors: {writer_names[0]: [], writer_names[1]: [], writer_names[2]: []},
                                   genres: {genra_names[0]: [], genra_names[1]: [], genra_names[2]: []}},
                   NSW_PP_books_path: {authors: {writer_names[0]: [], writer_names[1]: [], writer_names[2]: []},
                                   genres: {genra_names[0]: [], genra_names[1]: [], genra_names[2]: []}}}

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

def Pre_process_books():

    for book_class in book_classes:

        for class_name in os.listdir(f"{books_path}\{book_class}"):

            temp_book_names = os.listdir(f"{books_path}\{book_class}\{class_name}")

            for temp_book_name in temp_book_names:

                f = open(f"{books_path}\{book_class}\{class_name}\{temp_book_name}", 'r', encoding='utf-8', errors='replace')

                temp_text = ""

                for line in f.readlines():

                    temp_text += line

                f.close()

                original_text = temp_text

                # preprocessing
                temp_text = Preproces(original_text, False)

                # saving the file
                f = open(f"{PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'w', encoding='utf-8')
                f.write(temp_text)

                f.close()


                # preprocessing
                temp_text = Preproces(original_text, True)

                # saving the file
                f = open(f"{NSW_PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'w', encoding='utf-8')
                f.write(temp_text)

                f.close()

def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    return freq

def MergeDictionary(dic1, dic2):

    for item in dic2:

        if (item in dic1):

            dic1[item] += dic2[item]

        else:

            dic1[item] = dic2[item]

    return dic1

def Vocabulary_counter(word_list, step_size):

    keep_counting = True
    step_count = 1

    counts_list = []

    while (step_count * step_size < len(word_list)):

        temp_set = set(word_list[:step_count * step_size])
        counts_list.append(len(temp_set))

        step_count += 1

    temp_set = set(word_list)
    counts_list.append(len(temp_set))

    return counts_list



def Part_e():
    # for only pre processed books
    for book_class in book_classes:

        for class_name in os.listdir(f"{PP_books_path}\{book_class}"):

            temp_book_names = os.listdir(f"{PP_books_path}\{book_class}\{class_name}")

            for temp_book_name in temp_book_names:
                f = open(f"{PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'r', encoding='utf-8')

                temp_text = ""

                for line in f.readlines():
                    temp_text += line

                f.close()

                temp_text_words = temp_text.split()

                temp_dictinory = CountFrequency(temp_text_words)

                temp_sorted_dictionary = {k: v for k, v in sorted(temp_dictinory.items(), key=lambda item: item[1], reverse=True)}

                vocabulary_file[PP_books_path][book_class][class_name].append(temp_sorted_dictionary)

    """
    # for pre processed and stop word removed books
    for book_class in book_classes:

        for class_name in os.listdir(f"{NSW_PP_books_path}\{book_class}"):

            temp_book_names = os.listdir(f"{NSW_PP_books_path}\{book_class}\{class_name}")

            for temp_book_name in temp_book_names:
                f = open(f"{NSW_PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'r', encoding='utf-8')

                temp_text = ""

                for line in f.readlines():
                    temp_text += line

                f.close()

                temp_text_words = temp_text.split()

                temp_dictinory = CountFrequency(temp_text_words)

                temp_sorted_dictionary = {k: v for k, v in sorted(temp_dictinory.items(), key=lambda item: item[1], reverse=True)}

                vocabulary_file[NSW_PP_books_path][book_class][class_name].append(temp_sorted_dictionary)
    """

def Part_f():

    # creating the merge of books of each author
    preprocess_type = "PP_books"
    book_class = "Authors"
    for class_name in vocabulary_file[preprocess_type][book_class]:

        temp_sumed_dictionary = {}

        for dictionary in vocabulary_file[preprocess_type][book_class][class_name]:

            temp_sumed_dictionary = MergeDictionary(temp_sumed_dictionary, dictionary)


        temp_sorted_dictionary = {k: v for k, v in sorted(temp_sumed_dictionary.items(), key=lambda item: item[1], reverse=True)}

        vocabulary_file[preprocess_type][book_class][class_name].append(temp_sorted_dictionary)


    # ploting the linear plot for authers
    legend_names = []
    for class_name in vocabulary_file[preprocess_type][book_class]:

        legend_names.append(class_name)

        dictinory = vocabulary_file[preprocess_type][book_class][class_name][3]

        freqs = list(dictinory.values())
        ranks = list(range(1, len(dictinory.keys()) + 1))

        plt.scatter(ranks, freqs, s=0.8, label=class_name)


    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Linear Plot for the Different Authers")
    plt.legend(legend_names)
    plt.show()


    # ploting the log-log plot for authers
    legend_names = []
    for class_name in vocabulary_file[preprocess_type][book_class]:

        legend_names.append(class_name)

        dictinory = vocabulary_file[preprocess_type][book_class][class_name][3]

        freqs = list(dictinory.values())
        ranks = list(range(1, len(dictinory.keys()) + 1))

        plt.scatter(np.log(ranks), np.log(freqs), s=0.8, label=class_name)


    plt.xlabel("log(Rank)")
    plt.ylabel("log(Frequency)")
    plt.title("Log-Log Plot for the Different Authers")
    plt.legend(legend_names)
    plt.show()


    # ploting the log-log plots for each authers books
    for class_name in vocabulary_file[preprocess_type][book_class]:

        legend_names = os.listdir(f"{preprocess_type}\{book_class}\{class_name}")
        legend_names = [name.split("by")[0] for name in legend_names]

        for i in range(3):
            dictinory = vocabulary_file[preprocess_type][book_class][class_name][i]

            freqs = list(dictinory.values())
            ranks = list(range(1, len(dictinory.keys()) + 1))

            plt.scatter(np.log(ranks), np.log(freqs), s=0.8, label=class_name)

        plt.xlabel("log(Rank)")
        plt.ylabel("log(Frequency)")
        plt.title(f"Log-Log Plot for the Each Book of {class_name}")
        plt.legend(legend_names)
        plt.show()

def Part_g():

    # for only pre processed books
    for book_class in book_classes:

        for class_name in os.listdir(f"{PP_books_path}\{book_class}"):

            temp_text = ""

            temp_book_names = os.listdir(f"{PP_books_path}\{book_class}\{class_name}")

            for temp_book_name in temp_book_names:
                f = open(f"{PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'r', encoding='utf-8')

                for line in f.readlines():
                    temp_text += line

                f.close()

            temp_text_words = temp_text.split()

            temp_word_counts = Vocabulary_counter(temp_text_words, 5000)

            corpus_size_file[PP_books_path][book_class][class_name].append(temp_word_counts)




    #ploting the plots
    preprocess_type = "PP_books"
    book_class = "Authors"

    # ploting the linear plot for authers
    legend_names = []
    for class_name in corpus_size_file[preprocess_type][book_class]:

        legend_names.append(class_name)

        number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][0]
        number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

        plt.scatter(number_of_tokens, number_of_words_types , s=0.8, label=class_name)


    plt.xlabel("Number of Tokens")
    plt.ylabel("Number of Word Types")
    plt.title("Linear Plot for the Different Authers")
    plt.legend(legend_names)
    plt.show()

    # ploting the log-log plot for authers
    legend_names = []
    for class_name in corpus_size_file[preprocess_type][book_class]:

        legend_names.append(class_name)

        number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][0]
        number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

        plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "-o", label=class_name)


    plt.xlabel("log(Number of Tokens)")
    plt.ylabel("log(Number of Word Types)")
    plt.title("Log-Log Plot for the Different Authers")
    plt.legend(legend_names)
    plt.show()

def Part_h_i():

    # for only pre processed books
    for book_class in book_classes:

        for class_name in os.listdir(f"{PP_books_path}\{book_class}"):

            temp_book_names = os.listdir(f"{PP_books_path}\{book_class}\{class_name}")

            for temp_book_name in temp_book_names:

                temp_text = ""

                f = open(f"{PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'r', encoding='utf-8')

                for line in f.readlines():
                    temp_text += line

                f.close()

                temp_text_words = temp_text.split()

                temp_word_counts = Vocabulary_counter(temp_text_words, 5000)

                corpus_size_file[PP_books_path][book_class][class_name].append(temp_word_counts)

                #calculating the slope:
                temp_number_of_tokens = np.array(range(1, len(temp_word_counts) + 1)) * 5000

                log_temp_word_counts = np.log(temp_word_counts)
                log_temp_number_of_tokens = np.log(temp_number_of_tokens)

                temp_slop, temp_bias = np.polyfit(log_temp_number_of_tokens, log_temp_word_counts, 1)

                corpus_size_slope_file[PP_books_path][book_class][class_name].append((temp_slop, temp_bias))




    #ploting the plots
    preprocess_type = "PP_books"
    book_class = "Authors"


    # ploting the log-log plots for each authers books
    for class_name in vocabulary_file[preprocess_type][book_class]:

        legend_names = os.listdir(f"{preprocess_type}\{book_class}\{class_name}")
        legend_names = [name.split("by")[0] for name in legend_names]

        for i in [-3, -2, -1]:

            number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][i]
            number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

            plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "o-", label=class_name)

            slope, bias = corpus_size_slope_file[preprocess_type][book_class][class_name][i]

            legend_names[i] += f", Slope: {slope:.3f}, Bias: {bias:.3f}"


        plt.xlabel("log(Number of Tokens)")
        plt.ylabel("log(Number of Word Types)")
        plt.title(f"Log-Log Plot for the Each Book of {class_name}")
        plt.legend(legend_names)
        plt.show()


    # ploting the log-log plots for all authers books
    colors = ["b", "g", "r"]
    color_index = 0

    legend_names = []
    curve_number = 0

    for class_name in vocabulary_file[preprocess_type][book_class]:

        temp_legend_names = os.listdir(f"{preprocess_type}\{book_class}\{class_name}")
        legend_names += [name.split(".txt")[0] for name in temp_legend_names]

        for i in [-3, -2, -1]:

            number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][i]
            number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

            plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "o-", color=colors[color_index], label=class_name)

            slope, bias = corpus_size_slope_file[preprocess_type][book_class][class_name][i]

            legend_names[curve_number] += f", Slope: {slope:.3f}, Bias: {bias:.3f}"

            curve_number += 1

        color_index += 1

    print("*** slope bias table for the only preprocesed authors ***")
    for i in legend_names:
        print(i)
    print("\n\n")

    plt.xlabel("log(Number of Tokens)")
    plt.ylabel("log(Number of Word Types)")
    plt.title(f"Log-Log Plot for the Each Book of all Authors")
    plt.legend(legend_names)
    plt.show()

def Part_j():

    #only filling the files if they are empty so we can run this part alone.
    if len(corpus_size_slope_file[PP_books_path][authors][writer_names[0]]) == 0:

        # for only pre processed books
        for book_class in book_classes:

            for class_name in os.listdir(f"{PP_books_path}\{book_class}"):

                temp_book_names = os.listdir(f"{PP_books_path}\{book_class}\{class_name}")

                for temp_book_name in temp_book_names:

                    temp_text = ""

                    f = open(f"{PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'r', encoding='utf-8')

                    for line in f.readlines():
                        temp_text += line

                    f.close()

                    temp_text_words = temp_text.split()

                    temp_word_counts = Vocabulary_counter(temp_text_words, 5000)

                    corpus_size_file[PP_books_path][book_class][class_name].append(temp_word_counts)

                    # calculating the slope:
                    temp_number_of_tokens = np.array(range(1, len(temp_word_counts) + 1)) * 5000

                    log_temp_word_counts = np.log(temp_word_counts)
                    log_temp_number_of_tokens = np.log(temp_number_of_tokens)

                    temp_slop, temp_bias = np.polyfit(log_temp_number_of_tokens, log_temp_word_counts, 1)

                    corpus_size_slope_file[PP_books_path][book_class][class_name].append((temp_slop, temp_bias))

        """
        # for pre processed and stop word removed books
        for book_class in book_classes:

            for class_name in os.listdir(f"{NSW_PP_books_path}\{book_class}"):

                temp_book_names = os.listdir(f"{NSW_PP_books_path}\{book_class}\{class_name}")

                for temp_book_name in temp_book_names:

                    temp_text = ""

                    f = open(f"{NSW_PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'r', encoding='utf-8')

                    for line in f.readlines():
                        temp_text += line

                    f.close()

                    temp_text_words = temp_text.split()

                    temp_word_counts = Vocabulary_counter(temp_text_words, 5000)

                    corpus_size_file[NSW_PP_books_path][book_class][class_name].append(temp_word_counts)

                    # calculating the slope:
                    temp_number_of_tokens = np.array(range(1, len(temp_word_counts) + 1)) * 5000

                    log_temp_word_counts = np.log(temp_word_counts)
                    log_temp_number_of_tokens = np.log(temp_number_of_tokens)

                    temp_slop, temp_bias = np.polyfit(log_temp_number_of_tokens, log_temp_word_counts, 1)

                    corpus_size_slope_file[NSW_PP_books_path][book_class][class_name].append((temp_slop, temp_bias))
        """

    # ploting the plots
    preprocess_type = "PP_books"
    book_class = "Types"

    # ploting the log-log plots for each type books
    for class_name in vocabulary_file[preprocess_type][book_class]:

        legend_names = os.listdir(f"{preprocess_type}\{book_class}\{class_name}")
        legend_names = [name.split(".txt")[0] for name in legend_names]

        for i in [-3, -2, -1]:
            number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][i]
            number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

            plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "o-", label=class_name)

            slope, bias = corpus_size_slope_file[preprocess_type][book_class][class_name][i]

            legend_names[i] += f", Slope: {slope:.3f}, Bias: {bias:.3f}"

        plt.xlabel("log(Number of Tokens)")
        plt.ylabel("log(Number of Word Types)")
        plt.title(f"Log-Log Plot for the Each {class_name} Book")
        plt.legend(legend_names)
        plt.show()



    # ploting the log-log plots for each all types of books
    colors = ["b", "g", "r"]
    color_index = 0

    legend_names = []
    curve_number = 0

    for class_name in vocabulary_file[preprocess_type][book_class]:

        temp_legend_names = os.listdir(f"{preprocess_type}\{book_class}\{class_name}")
        legend_names += [name.split(".txt")[0] for name in temp_legend_names]

        for i in [-3, -2, -1]:
            number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][i]
            number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

            plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "o-", color=colors[color_index], label=class_name)

            slope, bias = corpus_size_slope_file[preprocess_type][book_class][class_name][i]

            legend_names[curve_number] += f" ({class_name}), Slope: {slope:.3f}, Bias: {bias:.3f}"

            curve_number += 1

        color_index += 1

    print("*** slope bias table for the only preprocesed authors ***")
    for i in legend_names:
        print(i)
    print("\n\n")

    plt.xlabel("log(Number of Tokens)")
    plt.ylabel("log(Number of Word Types)")
    plt.title(f"Log-Log Plot for the Each Book of all Authors")
    plt.legend(legend_names)
    plt.show()

def Part_l():

    # **************************
    # *** creating the files ***
    # **************************
    # part e
    # for pre processed and stop word removed books
    for book_class in book_classes:

        for class_name in os.listdir(f"{NSW_PP_books_path}\{book_class}"):

            temp_book_names = os.listdir(f"{NSW_PP_books_path}\{book_class}\{class_name}")

            for temp_book_name in temp_book_names:
                f = open(f"{NSW_PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'r', encoding='utf-8')

                temp_text = ""

                for line in f.readlines():
                    temp_text += line

                f.close()

                temp_text_words = temp_text.split()

                temp_dictinory = CountFrequency(temp_text_words)

                temp_sorted_dictionary = {k: v for k, v in sorted(temp_dictinory.items(), key=lambda item: item[1], reverse=True)}

                vocabulary_file[NSW_PP_books_path][book_class][class_name].append(temp_sorted_dictionary)

    # part g
    # for pre processed and stop word removed books
    for book_class in book_classes:

        for class_name in os.listdir(f"{NSW_PP_books_path}\{book_class}"):

            temp_text = ""

            temp_book_names = os.listdir(f"{NSW_PP_books_path}\{book_class}\{class_name}")

            for temp_book_name in temp_book_names:
                f = open(f"{NSW_PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'r', encoding='utf-8')

                for line in f.readlines():
                    temp_text += line

                f.close()

            temp_text_words = temp_text.split()

            temp_word_counts = Vocabulary_counter(temp_text_words, 5000)

            corpus_size_file[NSW_PP_books_path][book_class][class_name].append(temp_word_counts)

    # part h_i
    # for pre processed and stop word removed books
    for book_class in book_classes:

        for class_name in os.listdir(f"{NSW_PP_books_path}\{book_class}"):

            temp_book_names = os.listdir(f"{NSW_PP_books_path}\{book_class}\{class_name}")

            for temp_book_name in temp_book_names:

                temp_text = ""

                f = open(f"{NSW_PP_books_path}\{book_class}\{class_name}\{temp_book_name}", 'r', encoding='utf-8')

                for line in f.readlines():
                    temp_text += line

                f.close()

                temp_text_words = temp_text.split()

                temp_word_counts = Vocabulary_counter(temp_text_words, 5000)

                corpus_size_file[NSW_PP_books_path][book_class][class_name].append(temp_word_counts)

                #calculating the slope:
                temp_number_of_tokens = np.array(range(1, len(temp_word_counts) + 1)) * 5000

                log_temp_word_counts = np.log(temp_word_counts)
                log_temp_number_of_tokens = np.log(temp_number_of_tokens)

                temp_slop, temp_bias = np.polyfit(log_temp_number_of_tokens, log_temp_word_counts, 1)

                corpus_size_slope_file[NSW_PP_books_path][book_class][class_name].append((temp_slop, temp_bias))



    # *************************
    # *** drawing the plots ***
    # *************************
    # part f
    # creating the merge of books of each author
    preprocess_type = "NSW_PP_books"
    book_class = "Authors"
    for class_name in vocabulary_file[preprocess_type][book_class]:

        temp_sumed_dictionary = {}

        for dictionary in vocabulary_file[preprocess_type][book_class][class_name]:

            temp_sumed_dictionary = MergeDictionary(temp_sumed_dictionary, dictionary)


        temp_sorted_dictionary = {k: v for k, v in sorted(temp_sumed_dictionary.items(), key=lambda item: item[1], reverse=True)}

        vocabulary_file[preprocess_type][book_class][class_name].append(temp_sorted_dictionary)


    # ploting the linear plot for authers
    legend_names = []
    for class_name in vocabulary_file[preprocess_type][book_class]:

        legend_names.append(class_name)

        dictinory = vocabulary_file[preprocess_type][book_class][class_name][3]

        freqs = list(dictinory.values())
        ranks = list(range(1, len(dictinory.keys()) + 1))

        plt.scatter(ranks, freqs, s=0.8, label=class_name)


    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Linear Plot for the Different Authers (No Stop Word)")
    plt.legend(legend_names)
    plt.show()


    # ploting the log-log plot for authers
    legend_names = []
    for class_name in vocabulary_file[preprocess_type][book_class]:

        legend_names.append(class_name)

        dictinory = vocabulary_file[preprocess_type][book_class][class_name][3]

        freqs = list(dictinory.values())
        ranks = list(range(1, len(dictinory.keys()) + 1))

        plt.scatter(np.log(ranks), np.log(freqs), s=0.8, label=class_name)


    plt.xlabel("log(Rank)")
    plt.ylabel("log(Frequency)")
    plt.title("Log-Log Plot for the Different Authers (No Stop Word)")
    plt.legend(legend_names)
    plt.show()


    # ploting the log-log plots for each authers books
    for class_name in vocabulary_file[preprocess_type][book_class]:

        legend_names = os.listdir(f"{preprocess_type}\{book_class}\{class_name}")
        legend_names = [name.split("by")[0] for name in legend_names]

        for i in range(3):
            dictinory = vocabulary_file[preprocess_type][book_class][class_name][i]

            freqs = list(dictinory.values())
            ranks = list(range(1, len(dictinory.keys()) + 1))

            plt.scatter(np.log(ranks), np.log(freqs), s=0.8, label=class_name)

        plt.xlabel("log(Rank)")
        plt.ylabel("log(Frequency)")
        plt.title(f"Log-Log Plot for the Each Book of {class_name} (No Stop Word)")
        plt.legend(legend_names)
        plt.show()



    # part g
    #ploting the plots
    preprocess_type = "NSW_PP_books"
    book_class = "Authors"

    # ploting the linear plot for authers
    legend_names = []
    for class_name in corpus_size_file[preprocess_type][book_class]:

        legend_names.append(class_name)

        number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][0]
        number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

        plt.plot(number_of_tokens, number_of_words_types, "o-", label=class_name)


    plt.xlabel("Number of Tokens")
    plt.ylabel("Number of Word Types")
    plt.title("Linear Plot for the Different Authers (No Stop Word)")
    plt.legend(legend_names)
    plt.show()

    # ploting the log-log plot for authers
    legend_names = []
    for class_name in corpus_size_file[preprocess_type][book_class]:

        legend_names.append(class_name)

        number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][0]
        number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

        plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "o-", label=class_name)


    plt.xlabel("log(Number of Tokens)")
    plt.ylabel("log(Number of Word Types)")
    plt.title("Log-Log Plot for the Different Authers (No Stop Word)")
    plt.legend(legend_names)
    plt.show()


    # part h_i
    #ploting the plots
    preprocess_type = "NSW_PP_books"
    book_class = "Authors"


    # ploting the log-log plots for each authers books
    for class_name in vocabulary_file[preprocess_type][book_class]:

        legend_names = os.listdir(f"{preprocess_type}\{book_class}\{class_name}")
        legend_names = [name.split("by")[0] for name in legend_names]

        for i in [-3, -2, -1]:

            number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][i]
            number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

            plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "o-", label=class_name)

            slope, bias = corpus_size_slope_file[preprocess_type][book_class][class_name][i]

            legend_names[i] += f", Slope: {slope:.3f}, Bias: {bias:.3f}"

        plt.xlabel("log(Number of Tokens)")
        plt.ylabel("log(Number of Word Types)")
        plt.title(f"Log-Log Plot for the Each Book of {class_name} (No Stop Word)")
        plt.legend(legend_names)
        plt.show()


    # ploting the log-log plots for all authers books
    colors = ["b", "g", "r"]
    color_index = 0

    legend_names = []
    curve_number = 0

    for class_name in vocabulary_file[preprocess_type][book_class]:

        temp_legend_names = os.listdir(f"{preprocess_type}\{book_class}\{class_name}")
        legend_names += [name.split(".txt")[0] for name in temp_legend_names]

        for i in [-3, -2, -1]:

            number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][i]
            number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

            plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "o-", color=colors[color_index], label=class_name)

            slope, bias = corpus_size_slope_file[preprocess_type][book_class][class_name][i]

            legend_names[curve_number] += f", Slope: {slope:.3f}, Bias: {bias:.3f}"

            curve_number += 1

        color_index += 1

    print("*** slope bias table for the preprocesed and (No Stop Word) authors ***")
    for i in legend_names:
        print(i)
    print("\n\n")

    plt.xlabel("log(Number of Tokens)")
    plt.ylabel("log(Number of Word Types)")
    plt.title(f"Log-Log Plot for the Each Book from All Types (No Stop Word) ")
    plt.legend(legend_names)
    plt.show()





    # part j
    # ploting the plots
    preprocess_type = "NSW_PP_books"
    book_class = "Types"

    # ploting the log-log plots for each type books
    for class_name in vocabulary_file[preprocess_type][book_class]:

        legend_names = os.listdir(f"{preprocess_type}\{book_class}\{class_name}")
        legend_names = [name.split(".txt")[0] for name in legend_names]

        for i in [-3, -2, -1]:
            number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][i]
            number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

            plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "o-", label=class_name)

            slope, bias = corpus_size_slope_file[preprocess_type][book_class][class_name][i]

            legend_names[i] += f", Slope: {slope:.3f}, Bias: {bias:.3f}"

        plt.xlabel("log(Number of Tokens)")
        plt.ylabel("log(Number of Word Types)")
        plt.title(f"Log-Log Plot for the Each {class_name} Book (No Stop Word) ")
        plt.legend(legend_names)
        plt.show()

    # ploting the log-log plots for each all types of books
    colors = ["b", "g", "r"]
    color_index = 0

    legend_names = []
    curve_number = 0

    for class_name in vocabulary_file[preprocess_type][book_class]:

        temp_legend_names = os.listdir(f"{preprocess_type}\{book_class}\{class_name}")
        legend_names += [name.split(".txt")[0] for name in temp_legend_names]

        for i in [-3, -2, -1]:
            number_of_words_types = corpus_size_file[preprocess_type][book_class][class_name][i]
            number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

            plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "o-", color=colors[color_index], label=class_name)

            slope, bias = corpus_size_slope_file[preprocess_type][book_class][class_name][i]

            legend_names[curve_number] += f" ({class_name}), Slope: {slope:.3f}, Bias: {bias:.3f}"

            curve_number += 1

        color_index += 1

    print("*** slope bias table for the preprocesed and (No Stop Word) book types ***")
    for i in legend_names:
        print(i)
    print("\n\n")

    plt.xlabel("log(Number of Tokens)")
    plt.ylabel("log(Number of Word Types)")
    plt.title(f"Log-Log Plot for the Each Book of all Authors (No Stop Word) ")
    plt.legend(legend_names)
    plt.show()

def Random_corpus_generator():

    alfabe = "abcdefghijklmnopqrstuvwxyz "

    random_corpora = ''.join(rd.choice(alfabe) for _ in range(2500000))
    f = open(f"{random_corpus_file_name}", 'w', encoding='utf-8')
    f.write(random_corpora)
    f.close()

def Part_m():

    temp_text = ""

    f = open(f"{random_corpus_file_name}", 'r', encoding='utf-8')

    for line in f.readlines():
        temp_text += line

    f.close()

    temp_text_words = temp_text.split()

    # ploting the log(token count) vs. log(corpus size) plot for random corpus
    number_of_words_types = Vocabulary_counter(temp_text_words, 5000)
    number_of_tokens = np.array(range(1, len(number_of_words_types) + 1)) * 5000

    plt.plot(np.log(number_of_tokens), np.log(number_of_words_types), "o-", label="Random Corpus")
    plt.xlabel("log(Number of Tokens)")
    plt.ylabel("log(Number of Word Types)")
    plt.title("Log-Log Plot of token count vs. corpus sizefor the Randomly Generated Corpus")
    plt.show()

    # ploting the token count vs. corpus size plot for random corpus
    plt.plot(number_of_tokens, number_of_words_types, "o-", label="Random Corpus")
    plt.xlabel("Number of Tokens")
    plt.ylabel("Number of Word Types")
    plt.title("linear Plot of token count vs. corpus size for the Randomly Generated Corpus")
    plt.show()



    dictinory = CountFrequency(temp_text_words)
    sorted_dictionary = {k: v for k, v in sorted(dictinory.items(), key=lambda item: item[1], reverse=True)}
    freqs = list(sorted_dictionary.values())
    ranks = list(range(1, len(sorted_dictionary.keys()) + 1))


    # ploting the linear Zips law plot for random corpus
    plt.scatter(ranks, freqs, s=0.8, label="Randomly Generated Corpus")
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Linear Zipf's Law Plot for the the Randomly Generated Corpus")
    plt.show()


    # ploting the log-log Zips law plot for random corpus
    plt.scatter(np.log(ranks), np.log(freqs), s=0.8, label="Randomly Generated Corpus")
    plt.xlabel("log(Rank)")
    plt.ylabel("log(Frequency)")
    plt.title("Log-Log Zipf's Law Plot for the the Randomly Generated Corpus")
    plt.show()



#pre_process_books()


#Part_e() # creats vocabulary files carrying the word types along with their frequencies.

#Part_f() # plots vocabulary files carrying the word types along with their frequencies.

#Part_g() # creats type-token files for combined corpora and plots it

#Part_h_i() # creats type-token files for each book, finds their slops and plots it for authers

#Part_j() # creats type-token files for each book, finds their slops and plots it for book types

#Part_l() # does all the previus parts but for the no stop word corpus.


Random_corpus_generator()

Part_m() # plot the type-token for the randomly generated corpora


print("I am happy!!")
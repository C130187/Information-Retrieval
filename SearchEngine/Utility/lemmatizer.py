# -*- coding: utf-8 -*-
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Lemmatiser(object):
    def __init__(self):
        self.lemmatiser = WordNetLemmatizer()
        self.stopwords = set(stopwords.words("english"))

    def eliminate_stop_words(self, word_list):
        filtered_word_list = [word for word in word_list if word not in self.stopwords]
        return filtered_word_list

    def eliminate_punctuators(self, text):
        #text = text.replace('–'.decode('utf8'), '')
        text = text.replace('’', "")
        text = text.replace('"', '')
        text = text.replace('“', '')
        text = text.replace('”', '')
        text = text.replace(':', ' ')
        #text = text.replace('-', '')
        return text

    def generate_token_stream(self, text):
        words = word_tokenize(text)
        return words

    def lemmatize_word(self, word_list, mode='a'):
        """
        Lemmatizes the list of words
        :param word_list: List of all the words
        :return: the lemmatized version of the words
        """
        lemmatized_list = []
        for item in word_list:
            lemmatized_list.append(self.lemmatiser.lemmatize(item, mode))
        return lemmatized_list


def main():
    le = Lemmatiser()
    text = 'Roger Federer will compete for his 18th grand slam singles title - after defeating : countryman Stan Wawrinka in a gripping five-set Australian Open semi-final at Rod Laver Arena.'
    text = le.eliminate_punctuators(text)
    text = le.generate_token_stream(text)
    print text
    text = le.lemmatize_word(text)
    print text
    #crawl.crawl_query('Nadal')
    #query = 'Rafael'
    #print query
    #query=query.replace(" ", "%20")
    #print query

if __name__ == '__main__':
    main()

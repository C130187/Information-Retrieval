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

    def generate_token_stream(self, text):
        words = word_tokenize(text)
        return words

    def lemmatize_word(self, word_list):
        """
        Lemmatizes the list of words
        :param word_list: List of all the words
        :return: the lemmatized version of the words
        """
        lemmatized_list = []
        for item in word_list:
            lemmatized_list.append(self.lemmatiser.lemmatize(item, 'a'))
        return lemmatized_list
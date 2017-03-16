from nltk.tokenize import sent_tokenize, word_tokenize, line_tokenize
from nltk.corpus   import stopwords
from nltk.stem     import WordNetLemmatizer


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

    def lemmatizeWord(self, lst):
        """ Lemmatize the list of words.
        :param words: List of all the words
        :return: the lemmatized version of the words
        """
        lemmatized_list = []
        for item in lst:
            lemmatized_list.append(self.lemmatiser.lemmatize(item, 'a'))
        return lemmatized_list


example_text = 'Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard.'

example = "This is an example showing stopword filtration."

lemmatiser = Lemmatiser()
y = lemmatiser.generate_token_stream('Cats are better when eaten with milk.')
print
print "Lemmatising"
print lemmatiser.lemmatizeWord(y)

words = word_tokenize(example)

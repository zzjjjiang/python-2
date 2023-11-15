class WordCounter:
    def __init__(self, sentence):
        self.sentence=sentence
        self.__wordcount=0
        self.__words=self.sentence.split(" ")
    def count_words(self):
        self.__wordcount=len(self.__words)
    def get_word_count(self):
        return self.__wordcount
    def get_shortest_word(self):
        return min(map(lambda w: len(w), self.__words))
    def get_longest_word(self):
        return max(map(lambda w: len(w), self.__words))
    
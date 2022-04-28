# encoding: utf-8
from configuration.config import PUNCTUATION, STOP_WORDS
from unidecode import unidecode


class Parser:

    """ Represents the parser"""
    def __init__(self, question):
        self.question = question
        self.delete_punctuation()
        self.remove_accents()
        self.remove_uppercase()
        self.get_question_into_list()
        self.remove_stop_words()

    """" Removes the punctuation """""
    def delete_punctuation(self):
        for oneCharacter in self.question:
            if oneCharacter in PUNCTUATION:
                self.question = self.question.replace(oneCharacter, " ")

    """ Remove the accents """
    def remove_accents(self):
        self.question = unidecode(self.question)

    """ Remove uppercase to match with stop words"""
    def remove_uppercase(self):
        self.question = self.question.lower()

    """ Changes phrase to list to remove stop words """
    def get_question_into_list(self):
        self.question = self.question.split()

    """ Removes stop words and create sentence """
    def remove_stop_words(self):
        allWordsAfterRemove =\
            [word for word in self.question if word not in STOP_WORDS]
        self.question = " ".join(allWordsAfterRemove)

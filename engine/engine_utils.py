
from time import time

class Library():
    def __init__(self) -> None:
        pass

class Collection():
    def __init__(self) -> None:
        pass

class Word():
    def __init__(self, word:str, translation:str, l_time:int=time()) -> None:
        self.word = word
        self.translation = translation
        self.last_time = l_time
        self.repeated = 0
        self.correct = 0
    
    def check_word(self, word:str) -> bool:
        """sumary_line"""
        self.repeated += 1
        self.last_time = time()
        if word == self.word:
            self.correct += 1
            return True
        else:
            return False

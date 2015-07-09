import re
from Markov import MarkovChain

class WordMarkovChain(MarkovChain):
    default_order = 3
    
    @staticmethod
    def parse(data):
        return filter(lambda x: x != '', re.split(r'[\.,;\?!\s\"]+', data))

    @staticmethod
    def unparse(data):
        return " ".join(data)
    
class CharMarkovChain(MarkovChain):
    default_order = 2

    @staticmethod
    def parse(data):
        return list(data)

    @staticmethod
    def unparse(data):
        return ''.join(data)

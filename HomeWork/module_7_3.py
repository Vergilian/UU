import re
from pprint import pprint


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    clean_words = re.sub(r'[^\w\s]', '', line).lower().split()
                    words.extend(clean_words)
            all_words[file_name] = words
        return all_words



    def find(self, word):
        word = word.lower()
        positions = {}
        for name, words in self.get_all_words().items():
            if word in words:
                positions[name] = words.index(word) + 1
            else:
                positions[name] = None
        return positions

    def count(self, word):
        word = word.lower()
        counts = {}
        for name, words in self.get_all_words().items():
            if word in words:
                counts[name] = words.count(word)
        return counts


finder1 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')

pprint(finder1.get_all_words(), compact=True)
print(finder1.find('captain'))
print(finder1.count('captain'))
print(finder1.find('TEXT')) # 3 слово по счёту
print(finder1.count('teXT')) # 4 слова teXT в тексте всего
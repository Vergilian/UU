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


w = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
# pprint(w.get_all_words(), compact=True)
print(w.find('TEXT'))

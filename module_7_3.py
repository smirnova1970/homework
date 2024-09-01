import io
from pprint import pprint
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_names in self.file_names:
            with open(file_names, 'r', encoding='utf-8') as file:
                new = file.read().lower()
                for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    new = new.replace(symbol, ' ')
                words = new.split()
                all_words[file_names] = words
        return all_words
                #print(all_words)

    def find(self, word):
        position = {}
        for i, j in self.get_all_words().items():
            if word.lower() in j:
                position[i] = j.index(word.lower()) + 1

        return position

    def count(self, word):
        guantity = {}
        for a,b in self.get_all_words().items():
            words_count = b.count(word.lower())
            guantity[a] = words_count

        return guantity


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())  # Все слова
# print(finder2.find('TEXT'))  # 3 слово по счёту
# print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))


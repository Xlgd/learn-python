import requests
from bs4 import BeautifulSoup

languages = ['', 'arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese',
             'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']
languages2 = ['', 'Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese',
              'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']


def write_to_file(content):
    with open(word + '.txt', 'w', encoding='utf-8') as f:
        for item in content:
            f.write(item)


class Translator:
    def __init__(self, from_language, to_language, word):
        self.from_language = from_language
        self.to_language = to_language
        self.word = word
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
        self.headers = {'User-Agent': self.user_agent}
        self.soup = None
        self.result = []

    def main(self):
        if self.to_language == 0:
            languages_temp = [item for item in languages if item != languages[self.from_language] and item != '']
            # print(languages_temp)
            for language in languages_temp:
                url = 'https://context.reverso.net/translation/' + languages[self.from_language] + '-' \
                      + language + '/' + self.word
                # print('parse', url)
                return_words, return_examples = self.translate(url)
                self.write_to_list(language, return_words, return_examples)
                # print('done')
        else:
            url = 'https://context.reverso.net/translation/' + languages[source_language] + '-' \
                  + languages[target_language] + '/' + word
            return_words, return_examples = self.translate(url)
            self.write_to_list(languages2[self.to_language], return_words, return_examples)
        for item in self.result:
            print(item, end='')
        write_to_file(self.result)

    def translate(self, address):
        r = requests.get(address, headers=self.headers)
        self.soup = BeautifulSoup(r.content, 'html.parser')
        result_words = self.parse_html("#translations-content > a:is(.translation, .ltr, .dict, .rtl)", "translations")
        result_examples = self.parse_html("div.example > div:is(.ltr, .rtl) > span.text", "examples")
        return result_words, result_examples

    def write_to_list(self, to_language, words, examples):
        language_part2 = to_language[0].upper() + to_language[1:]
        self.result.append('\n' + language_part2 + ' Translations:\n' + words[0] + '\n\n'
                           + language_part2 + ' Examples:\n' + examples[0] + ':' + '\n' + examples[1] + '\n\n')

    def parse_html(self, path, keyword):
        html = self.soup.select(path)
        all_things = []
        for item in html:
            all_things.append(item.text.strip().replace('\n', ''))
        if keyword == 'translations':
            return [all_things[0]]
        elif keyword == 'examples':
            return [all_things[0], all_things[1]]


print("Hello, you're welcome to the translator. Translator supports:")
print('1. Arabic\n2. German\n3. English\n4. Spanish\n5. French\n6. Hebrew\n7. Japanese')
print('8. Dutch\n9. Polish\n10. Portuguese\n11. Romanian\n12. Russian\n13. Turkish')
print('Type the number of your language:')
source_language = int(input())
print("Type the number of a language you want to translate to or '0' to translate to all languages:")
target_language = int(input())
print('Type the word you want to translate:')
word = input()

T = Translator(source_language, target_language, word)
T.main()

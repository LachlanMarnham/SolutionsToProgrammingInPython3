from random import choice, randint

ARTICLES = ('the', 'a', 'an', 'one')
SUBJECTS = ('cat', 'dog', 'man', 'woman', 'aligator', 'emu', 'iguana',
            'octopus', 'urial')
VERBS = ('sang', 'ran', 'jumped')
ADVERBS = ('loudly', 'quietly', 'well', 'badly')
VOWELS = ('a', 'e', 'i', 'o', 'u')


def get_words():
    words = {'subject': choice(SUBJECTS),
             'verb': choice(VERBS),
             'adverb': choice(ADVERBS)
             }
    article = choice(ARTICLES)
    # subjects starting with a vowel/consonant should not follow 'a'/'an'
    if article == 'a' and words['subject'].startswith(VOWELS):
        article = 'an'
    elif article == 'an' and not words['subject'].startswith(VOWELS):
        article = 'a'
    words['article'] = article
    # Remove adverb if randint() returns 1
    if randint(0, 1):
        words.pop('adverb')
    return words


def make_line(words):
    line = words['article'] + ' ' + words['subject'] + ' ' + words['verb']
    if 'adverb' in words:
        line += ' ' + words['adverb']
    return line


def make_poem(number_of_lines):
    lines = []
    for i in range(number_of_lines):
        words_in_line = get_words()
        # The final line should end with a full stop, and all other lines
        # end in commas.
        if i == number_of_lines - 1:
            lines.append(make_line(words_in_line) + '.')
        else:
            lines.append(make_line(words_in_line) + ',')
    # The poem should begin with a capital letter
    return '\n'.join(lines).capitalize()


while True:
    user_input = input('Enter poem length between 1 and 10 lines: ')
    try:
        poem_length = int(user_input)
        if not 0 < poem_length <= 10:
            raise ValueError
    except ValueError:
        if user_input == '':
            poem_length = 5
        else:
            print('Invalid input. Please try again.')
            continue
    print(make_poem(poem_length))
    break

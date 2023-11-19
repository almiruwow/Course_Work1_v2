import random
from morse import morse


def get_random_word(words):
    """
    Получает рандомное слово из списка
    """
    word = random.choice(words)
    return word


def morse_encode(word):
    """
    переводит слова на английском языке в последовательности точек и тирe
    """

    new_word = ''

    for w in word:
        new_word += morse[w]

    return new_word


def print_statistics(answers):
    """
    Выводит статистику об игре
    """
    print(f'\nВсего задачек: {len(answers)}\n'
          f'Отвечено верно: {len(list(filter(lambda x: x==True, answers)))}\n'
          f'Отвечено неверно: {len(list(filter(lambda x: x==False, answers)))}')

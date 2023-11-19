from functions import get_random_word, morse_encode, print_statistics

words_list = ['code', 'bit', 'list', 'soul', 'next', 'skypro', 'skyeng']
answers = []

counter = 0
input('Сегодня мы потренируемся расшифровывать азбуку Морзе\nНажмите Enter и начнем\n')

while counter != 5:
    random = get_random_word(words_list)
    counter += 1

    secret = morse_encode(random)

    print(f'Слово {counter}: {secret}')

    user_input = input('Ваш ответ: ')

    if user_input == random:
        print(f'Верно, {random.title()}!')
        answers.append(True)
    else:
        print(f'Неверно, {random.title()}!')
        answers.append(False)


print_statistics(answers)
from utils import random_word, shuffle_word, score_record, get_statistic

def main():

    answer = 0

    user_name = print('Введите ваше имя')

    words = random_word()
    for word in words:
        answer += 1
        word_shaffled = shuffle_word(word)
        print(f'Угадай слово  {word_shaffled}')
        user_input = input()

        if user_input == word:
            print('Верно, вы получите 30 баллов')
        else:
            print(f'неправильно, правильный ответ {word}')
        print(answer)
    score_record(user_name, user_input)
    stats = get_statistic()
    print(f'Всего сыграно игра {stats.get("len")}')
    print(f'максимально быллов {stats.get("max")}')
main()
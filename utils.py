import random

def random_word():
    with open('word.txt', 'r', encoding="utf-8") as f:
        lines = f.read()
        words = lines.splitlines()
    return words

def shuffle_word(word):
    words_as_list = list(word)
    random.shuffle(words_as_list)
    return ''.join(words_as_list)

def score_record(player_name, player_score):
    with open('history.txt', 'a', encoding='utf-8') as f:
        f.write (f'имя {player_name} очки {player_score} \n')
def get_statistic():
    scores = []
    with open('history.txt', 'r', encoding='utf-8') as f:
        for line in f:
            score = line.strip().split(' ')
            scores.append(len(score))

    max_score =max(scores)
    len_score = len(score)

    return {'max':max_score, 'len':len_score }
#from utils import random_word, shuffle_word, score_record, get_statistic

def main():
    answer = 0
    print('Введите ваше имя')
    user_name = input()
    words =random_word()
    for word in words:
        word_shaffled = shuffle_word(word)
        print(f'Угадай слово  {word_shaffled}')
        user_input = input()

        if user_input == word:
            answer += 10
            print('Верно, вы получите 10 баллов')
        else:
            print(f'неправильно, правильный ответ {word}')

    score_record(user_name, answer)
    stats = get_statistic()
    print(f'Всего сыграно игра {stats.get("len")}')
    print(f'максимально быллов {stats.get("max")}')
main()

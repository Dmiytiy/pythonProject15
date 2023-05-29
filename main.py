name = input('введите своё имя ')
#программа выбирает первое слово из списка, перемешивет буквы, пользователь должен его отградать
with open('word.txt', 'r') as f:
    print(f.read())
    import random
    answers = 0 #Счётчик правильных ответов
    #надо заделить буквы в слове
    text_list = []  # создаем пустой список

    words = random_word()
    for word in words:
        word_shaffled = shuffle_word(word)
        print(f'Угsадай слово  {word_shaffled}')
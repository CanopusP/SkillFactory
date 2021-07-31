import numpy as np


def game_core_v2(number):
    count = 1
    predict = np.random.randint(1, 101)
    p1 = 101  # создание верхней границы
    p2 = 0  # создание нижней границы
    while number != predict:
        count += 1
        if number > predict:
            p2 = predict  # присвоение нижней границе значения попытки
            predict = predict + (p1 - p2) // 2  # присвоение нового значения попытке и смещение границы
        elif number < predict:
            p1 = predict  # присвоение верхней границе значения попытки
            predict = predict - (p1 - p2) // 2  # присвоение нового значения попытке и смещение границы
    return count  # выход из цикла, если угадали


def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v2)

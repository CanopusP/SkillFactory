#приветствие
def greetings():
    print("Это игра в крестики-нолики")
    print("Правила игры:")
    print("Игра идет на поле 3х3, игроки поочередно сводят Х и О на поле")
    print("Побеждает тот, кто сводит 3 своих элемента в ряд или по диагонали")
    print("Начало игры!!")
greetings()



#определение поля
board = list("-"*9)

def game_board():
    print(" ", "1", "2", "3")
    print("1", board[0], board[1], board[2])
    print("2", board[3], board[4], board[5])
    print("3", board[6], board[7], board[8])
game_board()

#определение победы
win = True

def result_of_game():
    global win
    win_position = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_position:
        if board[each[0]] == board[each[1]] == board[each[2]] == "X":
           print("Победитель определен! Победил 1-ый игрок")
           win = False
           return True
        elif board[each[0]] == board[each[1]] == board[each[2]] == "O":
           print("Победитель определен! Победил 2-ой игрок")
           win = False
           return True   
        elif all(elem != "-" for elem in board):
            print ("Победитель не определен! Ничья!")
            win = False
            return True
    return False

#функция ввода данных игроками
def request_player1():
    try:
        number = int(input("1-ый игрок, введите позицию на поле от 1 до 9: "))
        if board[number-1] != "-":
            print("Позиция занята!")
            request_player1()
        elif number not in range(1,10):
            print("Введите число от 1 до 9!")
            request_player1()
        else:
            board[number-1] = "X"
    except:
        print("Введите число от 1 до 9!")
        request_player1()

def request_player2():
    try:
        number = int(input("2-ой игрок, введите позицию на поле от 1 до 9: "))   
        if board[number-1] != "-":
            print("Позиция занята!")
            request_player2()
        elif number not in range(1,10):
            print("Введите число от 1 до 9!")
            request_player2()
        else:
            board[number-1] = "O"
    except:
        print("Введите число от 1 до 9!")
        request_player2()

#главная функция игры
while win:
    request_player1()
    game_board()
    result_of_game()
    if not win:
        break
    request_player2()
    game_board()
    result_of_game()

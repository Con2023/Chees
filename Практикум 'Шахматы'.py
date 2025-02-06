
count = 0
board = [ ["R", 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
         ["P", "P", "P", "P", "P", "P", "P", "P"],
          [" ", " ", " ", " ", " ", " ", " "," "],
          [" ", " ", " ", " ", " ", " ", " "," "],
          [" ", " ", " ", " ", " ", " ", " ", " "],
          [" ", " ", " ", " ", " ", " ", " ", " "],
          ["p", "p", "p", "p", "p", "p", "p", "p"],
          ["r", "n", "b", "k", "q", "b", "n", "r"]]
def print_board():
    """Функция выводит на печать шахматную доску"""
    print("   A B C D E F G H  ")
    print("   **************** ")
    for i in range(8):
        print(f"{i+1}* " + " ".join(board[i]))
    print("   ****************  ")
    print("   A B C D E F G H  ")

def get_coordinates(d):
    """Функция определяет координаты хода"""
    if d == 'MAT':
        check_move('MAT')
    elif d == 'BACK':
        check_move('BACK')
    else:
        letter = ord(d[0]) - ord('A')
        digit = int(d[1]) - 1
        return letter, digit #начала возвращается буква(координата) это х так как идкт столбики, начиная с 0 / число это у так как это строчки тоже с 0


def check_move(move):
    """Проверяем на корректность ввод пользователя"""
    if move == "MAT":
        return True
    if move == "BACK":
        return True
    if len(move.split()) != 2:
        return "Неверный ввод."
    elif move[0] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] or move[3] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G','H']:
        return "Неверный буквенный символ."
    elif move[1] not in ['1', '2', '3', '4', '5', '6', '7', '8'] or move[4] not in ['1', '2', '3', '4', '5', '6', '7','8']:
        return "Неверный числовой символ."
    else:
        return True


def check_fig(board, start_letterY, start_countX, current_player):
    """Функция проверяет наличие фигуры в начальной позиции"""
    fig = board[start_countX][start_letterY]
    if fig == " " :
        print("Здесь нет фигуры.")
        return False
    elif board[start_countX][start_letterY] in ["R", 'N', 'B', 'Q', 'K','P'] and current_player == "Чёрные" or board[start_countX][start_letterY] in ['p','k','q','b','n','r'] and current_player == "Белые":
        print("Эта фигура не твоя, будь внимательнее!")
        return False
    else:
        return True


def bishop(board, start_countX, start_letterY, end_letterY, end_countX):
    """Функция для всевозможных ходов"""
    count_diff = abs(end_countX - start_countX)
    let_diff = abs(end_letterY - start_letterY)
    #cлон
    if count_diff == let_diff:
        r = 1 if end_countX > start_countX else -1
        r1 = 1 if end_letterY > start_letterY else -1
        if board[start_countX][start_letterY] == 'b' and board[end_countX][end_letterY] == 'K':
            print("ШаХ!")
        if board[start_countX][start_letterY] == 'b' and board[end_countX][end_letterY] in ["R", 'N', 'B', 'Q','P', ' ']:
            for i in range(1, count_diff + 1):
                if board[start_countX + i * r][start_letterY + i * r1] == ' ' or board[start_countX + i * r][start_letterY + i * r1] in ["R", 'N', 'B', 'Q','P', 'K']:
                    return True
                else:
                    return False
        if board[start_countX][start_letterY] == 'B' and board[end_countX][end_letterY] == 'k':
            print("ШаХ!")
        if board[start_countX][start_letterY] == 'B' and board[end_countX][end_letterY] in ['p','q','b','n','r', ' ']:
            for i in range(1, count_diff + 1):
                if board[start_countX + i * r][start_letterY+ i * r1] == ' ' or board[start_countX + i * r][start_letterY+ i * r1] in ['p','q','b','n','r', 'k']:
                    return True
                else:
                    return False



def knight(board, start_countX, start_letterY, end_letterY, end_countX ):
    # #конь
    count_diff = abs(end_countX - start_countX)
    let_diff = abs(end_letterY - start_letterY)
    if count_diff == 2 and let_diff == 1 or count_diff == 1 and let_diff == 2:
        if board[end_countX][end_letterY] == 'K' or  board[end_countX][end_letterY] == 'k':
            print("ШаХ!")
        else:
            if board[start_countX][start_letterY] == 'n' and board[end_countX][end_letterY] in ["R", 'N', 'B' 'Q','P', ' ']:
                return True
            if board[start_countX][start_letterY] == 'N' and board[end_countX][end_letterY] in ['p','q','b','n','r', ' ']:
                return True



def rook (board, start_countX, start_letterY, end_letterY, end_countX):
    # Ладья
    count_diff = abs(end_countX - start_countX)
    let_diff = abs(end_letterY - start_letterY)
    if let_diff==0 and count_diff>0:
        r = 1 if end_countX > start_countX else -1
        if board[start_countX][start_letterY] == 'r' and board[end_countX][end_letterY] == 'K':
            print("ШаХ!")
        else:
            if board[start_countX][start_letterY] == 'r' and board[end_countX][end_letterY] in ["R", 'N', 'B', 'Q','P', ' ']:
                for i in range(1, count_diff + 1):
                    if board[start_countX + i * r][start_letterY] == ' 'and board[end_countX][end_letterY] in ["R", 'N', 'B', 'Q','P', ' ']:
                        return True
                    else:
                        return False
        if board[start_countX][start_letterY] == 'R' and board[end_countX][end_letterY] == 'k':
            print("ШаХ!")
        else:
            if board[start_countX][start_letterY] == 'R' and board[end_countX][end_letterY] in ['p','q','b','n','r',' ']:
                for i in range(1, count_diff + 1):
                    if board[start_countX + i * r][start_letterY] == ' ' and board[end_countX][end_letterY] in ['p','q','b','n','r', ' ']:
                        return True
                    else:
                        return False

    if count_diff == 0 and let_diff >0:
        r = 1 if end_letterY > start_letterY else -1
        if board[start_countX][start_letterY] == 'r' and board[end_countX][end_letterY] == 'K':
            print("ШаХ!")
        if board[start_countX][start_letterY] == 'r' and board[end_countX][end_letterY] in ["R", 'N', 'B', 'Q','P', " "]:
            for i in range(1, let_diff + 1):
                if board[start_countX][start_letterY + i * r] == ' ' or board[start_countX ][start_letterY + i * r] in ["R", 'N', 'B', 'Q','P','K']:
                    return True
                else:
                    return False
        if board[start_countX][start_letterY] == 'R' and board[end_countX][end_letterY] == 'k':
            print("ШаХ!")
        if board[start_countX][start_letterY] == 'R' and board[end_countX][end_letterY] in ['p','q','b','n','r', ' ']:
            for i in range(1, let_diff + 1):
                    if board[start_countX][start_letterY + i * r] == ' ' or board[start_countX][start_letterY + i * r] in ['p','q','b','n','r', 'k']:
                        return True
                    else:
                        return False


def queen(board, start_countX, start_letterY, end_letterY, end_countX):
    # #Королева
        count_diff = abs(end_countX - start_countX)
        let_diff = abs(end_letterY - start_letterY)
        r = 1 if end_countX > start_countX else -1
        r1 = 1 if end_letterY > start_letterY else -1

        if board[start_countX][start_letterY] == 'q' and board[end_countX][end_letterY] == 'K':
            print("Шах!")
        else:
            if board[start_countX][start_letterY] == 'q' and board[end_countX][end_letterY] in ["R", 'N', 'B', 'Q','P', ' ']:
                if count_diff == let_diff:
                    for i in range(1, count_diff + 1):
                        if board[start_countX + i * r][start_letterY + i * r1] == ' ' or board[start_countX + i * r][start_letterY + i * r1] in ["R", 'N', 'B', 'Q','P', 'K']:
                            return True
                        else:
                            return False

                if let_diff == 0 and count_diff > 0:
                    for i in range(1, count_diff + 1):
                        if board[start_countX + i * r][start_letterY] == ' 'or board[start_countX + i * r][start_letterY] in ["R", 'N', 'B', 'Q','P', 'K']:
                            return True
                        else:
                            return False
                if count_diff == 0 and let_diff > 0:
                    for i in range(1, let_diff + 1):
                        if board[start_countX][start_letterY + i * r] == ' '  or board[start_countX][start_letterY + i * r] in ["R", 'N', 'B', 'Q','P', 'K']:
                            return True
                        else:
                            return False

        if board[start_countX][start_letterY] == 'Q' and board[end_countX][end_letterY] == 'k':
            print("Шах!")
        else:
            if board[start_countX][start_letterY] == 'Q' and board[end_countX][end_letterY] in ['p','q','b','n','r', ' ']:
                if count_diff == let_diff:
                    for i in range(1, count_diff + 1):
                        if board[start_countX + i * r][start_letterY + i * r1] == ' ' or board[start_countX + i * r][start_letterY + i * r1] in ['p','k','q','b','n','r']:
                            return True
                        else:
                            return False

                if let_diff == 0 and count_diff > 0:
                    for i in range(1, count_diff + 1):
                        if board[start_countX + i * r][start_letterY] == ' ' or board[start_countX + i * r][start_letterY] in ['p','k','q','b','n','r']:
                            return True
                        else:
                            return False
                if count_diff == 0 and let_diff > 0:
                    for i in range(1, let_diff + 1):
                        if board[start_countX][start_letterY + i * r] == ' ' or board[start_countX][start_letterY + i * r] in ['p','k','q','b','n','r']:
                            return True
                        else:
                            return False



def king(board, start_countX, start_letterY, end_letterY, end_countX):
    # #Король
    count_diff = abs(end_countX - start_countX)
    let_diff = abs(end_letterY - start_letterY)
    if count_diff ==1 or let_diff == 1:
        if board[start_countX][start_letterY] == 'k' and board[end_countX][end_letterY] in ["R", 'N', 'B', 'Q', 'K','P', ' ']:
            return True
#происать в каждой функции шах, если оканичвается королем принутует ШАХ и не переносит фигуру!
# выпишем все условия с фигур которые выдают шах и король не может никуда походить мат.
        if board[start_countX][start_letterY] == 'K' and board[end_countX][end_letterY] in ['p','k','q','b','n','r', ' ']:
            return True



def pawns(board, start_countX, start_letterY, end_letterY, end_countX):
    #Пешка
    count_diff = abs(end_countX - start_countX)
    let_diff = abs(end_letterY - start_letterY)
    if board[start_countX][start_letterY] == 'P':
        if end_countX <= start_countX :
            print("Ошибка: пешка не может ходить назад")
            return False

        if board[start_countX][start_letterY] == 'p':
            if end_countX >= start_countX:
                print("Ошибка: пешка не может ходить назад")
                return False

    if end_letterY == start_letterY and ((count_diff == 1) or ((count_diff == 2 and start_countX == 1)) or ((count_diff == 2) and  (start_countX == 6))):
            for i in range(1, count_diff+1):
                r = 1 if end_countX > start_countX else -1
                if board[start_countX+ i*r ][start_letterY] != ' ' and board[start_countX + i*r][start_letterY] != '  ':
                    return False
            return True
    if count_diff == let_diff:
            for i in range(1, count_diff+1):
                if board[start_countX][start_letterY] == 'P':
                    if board[end_countX][end_letterY] in ['p','k','q','b','n','r']:
                        board[end_countX][end_letterY] = board[start_countX][start_letterY]
                        board[start_countX][start_letterY] = 'P'
                        print("Съедено, ням")

                        return True
                if board[start_countX][start_letterY] == 'p':
                    if board[end_countX][end_letterY] in ["R", 'N', 'B', 'Q', 'K','P']:
                        board[end_countX][end_letterY] = board[start_countX][start_letterY]
                        board[start_countX][start_letterY] = 'p'
                        print("Съедено, ням")

                        return True

def changging(board, start_countX, start_letterY, end_letterY, end_countX):
    board[end_countX][end_letterY] = board[start_countX][start_letterY]
    board[start_countX][start_letterY] = ' '
    return board



def request():
    """Запрос у игрока"""
    player_answer = input("Введите номер нужного действия\n1. Начать новую игру\n2. Загрузить игру\nЛюбой символ, кроме 1,2 завершает игру \n> ")
    return int (player_answer)


def mat(steps):
        with open('game_of_chess.txt', 'w', encoding='utf-8') as file:
            for ind, line in enumerate(steps, start=1):
                file.writelines(str(ind) + ' ' + line + '\n')

def back(a):
        w = a[::-1]
        w1, w2 = w[0].split(' ')
        res = w2 + ' ' + w1
        return str(res)

def load_game(file_path):

    with open(file_path, 'r') as f:
        c = f.readlines()
    return c

r = request()

current_player = 'Белые'
move = ' '
if r == 1:
    m = ''
    m1 = ''
    steps =[]
    b_st = []
    w_st =[]
    while True:
                print_board()
                move = input(f"{current_player} введите ход в формате [стартовая позиция][целевая позиция]: ").upper().strip()
                if check_move(move) is True:
                    if move == "MAT":
                        mat(steps)
                        break
                    if move == 'BACK':
                        if current_player == 'Белые':
                            print(w_st)
                            w1, w2 = w_st[len(w_st)-1].split(' ')
                            move = w2 + ' ' + w1
                            w_st.remove(w_st[len(w_st)-1])
                            start_letterY, start_countX = get_coordinates(move.split()[0])
                            end_letterY, end_countX = get_coordinates(move.split()[1])
                            if board[start_countX][start_letterY] == 'P' or board[start_countX][start_letterY] == 'B' or board[start_countX][start_letterY] == 'N' or board[start_countX][start_letterY] == 'R' or board[start_countX][start_letterY] == 'Q' or board[start_countX][start_letterY] == 'K' :
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    current_player = 'Чёрные'
                        elif current_player == 'Чёрные':
                            b1, b2 = b_st[len(b_st)-1].split(' ')
                            move1 = b2 + ' ' + b1
                            b_st.remove(b_st[len(b_st)-1])
                            start_letterY, start_countX = get_coordinates(move1.split()[0])
                            end_letterY, end_countX = get_coordinates(move1.split()[1])
                            if board[start_countX][start_letterY] == 'p' or board[start_countX][start_letterY] == 'b' or board[start_countX][start_letterY] == 'n' or board[start_countX][start_letterY] == 'r' or board[start_countX][start_letterY] == 'q' or board[start_countX][start_letterY] == 'k' :
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    current_player = 'Белые'

                    else:
                        start_letterY, start_countX = get_coordinates(move.split()[0])
                        end_letterY, end_countX = get_coordinates(move.split()[1])


                    if check_fig(board, start_letterY, start_countX, current_player) is True:
                        if board[start_countX][start_letterY] in ["R", 'N', 'B', 'Q', 'K','P'] and current_player == "Белые":
                            if  board[start_countX][start_letterY] == 'P':
                                    if pawns(board, start_countX, start_letterY, end_letterY, end_countX) is True:

                                        changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                        steps.append(move)
                                        w_st.append(move)
                                        count += 1

                                    else:
                                        print("Ход невозможен!")
                                        current_player = 'Чёрные'

                            elif board[start_countX][start_letterY] == 'B' :
                                if bishop(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    w_st.append(move)
                                else:
                                    print("Ход невозможен!")
                                    current_player = 'Чёрные'

                            elif board[start_countX][start_letterY] == 'N':
                                if knight(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    w_st.append(move)
                                else:
                                    print("Ход невозможен!")
                                    current_player = 'Чёрные'

                            elif board[start_countX][start_letterY] == 'R':
                                if rook(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    w_st.append(move)
                                else:
                                    print("Ход невозможен!")
                                    current_player = 'Чёрные'

                            elif  board[start_countX][start_letterY] == 'Q':
                                if queen(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    w_st.append(move)
                                else:
                                    print("Ход невозможен!")
                                    current_player = 'Чёрные'

                            elif board[start_countX][start_letterY] == 'K':
                                if king(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    w_st.append(move)
                                else:
                                    print("Ход невозможен!")
                                    current_player = 'Чёрные'


                        elif  board[start_countX][start_letterY] in ['p','k','q','b','n','r'] and current_player == "Чёрные":
                            if board[start_countX][start_letterY] == 'p' :
                                if pawns(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    b_st.append(move)
                                else:
                                    print("Ход невозможен!")
                                    current_player = 'Белые'

                            if  board[start_countX][start_letterY] == 'b':
                                if bishop(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    b_st.append(move)
                                else:
                                    print("Ход невозможен!")
                                    current_player = 'Белые'

                            if board[start_countX][start_letterY] == 'n' :
                                if knight(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    b_st.append(move)
                                else:
                                    print("Ход невозможен!")
                                    current_player = 'Белые'

                            if board[start_countX][start_letterY] == 'r':
                                if rook(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    b_st.append(move)
                                else:
                                    print("Ход невозможен!")
                                    current_player = 'Белые'

                            if board[start_countX][start_letterY] == 'q':
                                if queen(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    b_st.append(move)

                                else:
                                    print("Ход невозможен!")
                                    current_player = 'Белые'

                            if board[start_countX][start_letterY] == 'k':
                                if king(board, start_countX, start_letterY, end_letterY, end_countX) is True:
                                    changging(board, start_countX, start_letterY, end_letterY, end_countX)
                                    count += 1
                                    steps.append(move)
                                    b_st.append(move)
                                else:
                                    print("Король может передвигаться только на одну клетку.")
                                    current_player = 'Белые'

                        print(f'Число ходов: {count}')
                        if current_player == 'Белые':
                            current_player = 'Чёрные'
                        else:
                            current_player = 'Белые'

                else:
                    print("Неверный ввод. Попробуй еще раз.")

elif r == 2:
    file = load_game('Шахматыы.txt')
    moves = []
    for el in file:
        n_el = el[:5]
        moves.append(str(n_el))
    current_player = 'Белые'
    for i in moves:
                    if i == '#':
                        print("Игра завершена!")
                        break
                    move = i
                    r = input('')
                    start_letterY, start_countX = get_coordinates(move.split()[0])
                    end_letterY, end_countX = get_coordinates(move.split()[1])
                    if board[start_countX][start_letterY] in ["R", 'N', 'B', 'Q', 'K','P'] and current_player == "Белые":
                        if board[start_countX][start_letterY] == 'P':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Чёрные'
                            print_board()

                        if board[start_countX][start_letterY] == 'B':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Чёрные'
                            print_board()

                        if board[start_countX][start_letterY] == 'N':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Чёрные'
                            print_board()

                        if board[start_countX][start_letterY] == 'R':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Чёрные'
                            print_board()

                        if board[start_countX][start_letterY] == 'Q':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Чёрные'
                            print_board()

                        if board[start_countX][start_letterY] == 'K':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Чёрные'
                            print_board()

                    elif board[start_countX][start_letterY] in ['p', 'k', 'q', 'b', 'n','r'] and current_player == "Чёрные":
                        if board[start_countX][start_letterY] == 'p':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Белые'
                            print_board()

                        if board[start_countX][start_letterY] == 'b':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Белые'
                            print_board()

                        if board[start_countX][start_letterY] == 'n':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Белые'
                            print_board()

                        if board[start_countX][start_letterY] == 'r':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Белые'
                            print_board()

                        if board[start_countX][start_letterY] == 'q':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Белые'
                            print_board()

                        if board[start_countX][start_letterY] == 'k':
                            changging(board, start_countX, start_letterY, end_letterY, end_countX)
                            current_player = 'Белые'
                            print_board()

else:
    exit()






from itertools import chain
# Игровое поле


field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

# Сетка выбора игроков
move = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


# Проверка на выигрыш и на занятость поля
def WhoDidWin(y, x, p, player_id):
    while field[y][x] != '-':
        print('Поле уже занято')
        y = int(input("Выберите повторно поле по оси y: "))
        x = int(input("Выберите повторно поле по оси x: "))
    field[y][x] = p
    move[y][x] = player_id
    if move[0][0] == move[0][1] == move[0][2] != 0 or \
            move[1][0] == move[1][1] == move[1][2] != 0 or \
            move[2][0] == move[2][1] == move[2][2] != 0 or \
            move[0][0] == move[1][0] == move[2][0] != 0 or \
            move[0][1] == move[1][1] == move[2][1] != 0 or \
            move[0][2] == move[1][2] == move[2][2] != 0 or \
            move[0][0] == move[1][1] == move[2][2] != 0 or \
            move[0][2] == move[1][1] == move[2][0] != 0:
        return True


# Функция проверки на ничью
def Standoff():
    if 0 not in list(chain(*move)):
        return True
    else:
        return False


print("Приветствую вас в игре 'Крестики нолики!' ")
player_choice = ['x', '0']
print("Игроки выбирают за кого будут играть 'x(крестик) или 0(нолик)': ")
p1 = input("Выбор первого игрока: ")
p2 = input("Выбор второго игрока: ")

if p1 and p2 not in player_choice:
    print("Выбраны не правильные фигуры, попробуйте еще раз")
else:
    print("Выбраны правильные фигуры, игра начинается!!")
    # Начало игры
    while True:
        print(
            f"  0 1 2\n0 {field[0][0]} {field[0][1]} {field[0][2]}\n1 {field[1][0]} {field[1][1]} "
            f"{field[1][2]}\n2 {field[2][0]} {field[2][1]} {field[2][2]} \n ")

        # Ход первого игрока
        print(f"Ход первого игрока! - его фигура '{p1}'")
        y = int(input("Выберите поле по оси y: "))
        x = int(input("Выберите поле по оси x: "))

        if WhoDidWin(y, x, p1, 1):
            print("Победа!!")
            print(f"Выиграл первый игрок '{p1}'")
            print(
                f"  0 1 2\n0 {field[0][0]} {field[0][1]} {field[0][2]}\n1 {field[1][0]} {field[1][1]} "
                f"{field[1][2]}\n2 {field[2][0]} {field[2][1]} {field[2][2]} \n ")

            break

        if Standoff():
            print("Ничья!")
            break
        print(
            f"  0 1 2\n0 {field[0][0]} {field[0][1]} {field[0][2]}\n1 {field[1][0]} {field[1][1]} "
            f"{field[1][2]}\n2 {field[2][0]} {field[2][1]} {field[2][2]} \n ")

        # Ход второго игрока
        print(f"Ход второго игрока! - его фигура '{p2}'")
        y = int(input("Выберите поле по оси y: "))
        x = int(input("Выберите поле по оси x: "))

        if WhoDidWin(y, x, p2, 2):
            print("Победа!!")
            print(f"Выиграл второй игрок '{p2}'")
            print(
                f"  0 1 2\n0 {field[0][0]} {field[0][1]} {field[0][2]}\n1 {field[1][0]} {field[1][1]} "
                f"{field[1][2]}\n2 {field[2][0]} {field[2][1]} {field[2][2]} \n ")

            break
        if Standoff():
            print("Ничья!")
            break

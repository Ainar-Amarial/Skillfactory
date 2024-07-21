# # Модуль B5. Итоговое задание 5.6.1 (HW-02)

playing_field = [
    [" ", 1, 2, 3],
    [1, "-", "-", "-"],
    [2, "-", "-", "-"],
    [3, "-", "-", "-"]]

def move(X_or_O):
    while True:
        print("Ход", X_or_O)
        while True:
            x_coordinates, y_coordinates = input("Введите вертикальную координату: "), input("Введите горизонтальную координату: ")
            if x_coordinates.isdigit() and y_coordinates.isdigit():
                if int(x_coordinates) in [1, 2, 3] and int(y_coordinates) in [1, 2, 3]:
                    break
                else:
                    print("Вы вышли за пределы игрового поля")
            else:
                print("Введите число")
        x_coordinates, y_coordinates = int(x_coordinates), int(y_coordinates)
        coordinates = playing_field[x_coordinates][y_coordinates]
        if coordinates == "-":
            playing_field[x_coordinates][y_coordinates] = X_or_O
            break
        else:
            print("Это место занято")

    variant_1 = all(map(lambda x: x == X_or_O, [playing_field[1][1], playing_field[1][2], playing_field[1][3]]))
    variant_2 = all(map(lambda x: x == X_or_O, [playing_field[2][1], playing_field[2][2], playing_field[2][3]]))
    variant_3 = all(map(lambda x: x == X_or_O, [playing_field[3][1], playing_field[3][2], playing_field[3][3]]))
    variant_4 = all(map(lambda x: x == X_or_O, [playing_field[1][1], playing_field[2][1], playing_field[3][1]]))
    variant_5 = all(map(lambda x: x == X_or_O, [playing_field[1][2], playing_field[2][2], playing_field[3][2]]))
    variant_6 = all(map(lambda x: x == X_or_O, [playing_field[1][3], playing_field[2][3], playing_field[3][3]]))
    variant_7 = all(map(lambda x: x == X_or_O, [playing_field[1][1], playing_field[2][2], playing_field[3][3]]))
    variant_8 = all(map(lambda x: x == X_or_O, [playing_field[1][3], playing_field[2][2], playing_field[3][1]]))
    variant_all = any(map(lambda x: x == True, [variant_1, variant_2, variant_3, variant_4, variant_5, variant_6, variant_7, variant_8]))
    return variant_all

def drow_outcome():
    b = []
    for i in playing_field:
        for n in i:
            b.append(n)
    return ("-" not in b)

while True:
    for i in playing_field:
        print(*i)
    if move("X") == True:
        print("Победа Х")
        break
    if drow_outcome() == True:
        print("Ничья")
        break
    for i in playing_field:
        print(*i)
    if move("O") == True:
        print("Победа O")
        break
for i in playing_field:
    print(*i)

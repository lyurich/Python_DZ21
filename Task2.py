# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

summ = int(input("Введите количество журавликов: "))
p = summ // 6      # Количество журавликов, кторые сделал Петя
s = summ // 6        # Количество журавликов, кторые сделал Сережа
k = (summ // 6) * 4  # Количество журавликов, кторые сделала Катя

if summ != p + s + k:
    print('Задача не решается!')
else:
    print(f'Петя сделал {p} журавликов, Катя сделала {k} журавликов, Сережа сделал {s} журавликов.')
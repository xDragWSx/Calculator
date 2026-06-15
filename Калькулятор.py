import os
import time

print("         ===Calculator===      ")
print("|== Нажмите Enter для выключения ==|")

while True:
    print("-----------------------------------")
    print("| --- Новое вычисление --- |")
    print("|-- Ответ не должен быть кроме числа --|")
    print("|-- Введите первое число:")
    print()
    n1 = int(input())
    print()

    print("|--Введите второе число:")
    print()
    n2 = int(input())
    print()

    print("|-- Вычисление?")
    print("|-- 1 - Сумма")
    print("|-- 2 - Вычитание")
    print("|-- 3 - Умножение")
    print("|-- 4 - Деление")
    print()
    proc = int(input())
    print()

    # Сбрасываем ответ перед каждым вычислением
    ans = None

    if proc == 1:
        print("|-- Ваше текущее выражение:", n1, "+", n2)
        ans = n1 + n2
    elif proc == 2:
        print("|-- Ваше текущее выражение:", n1, "-", n2)
        ans = n1 - n2
    elif proc == 3:
        print("|-- Ваше текущее выражение:", n1, "*", n2)
        ans = n1 * n2
    elif proc == 4:
        print("|-- Какое деление вы хотите?")
        print("|-- 1 - ответ может быть не целым числом")
        print("|-- 2 - ответ целое число")
        print()
        pdel = int(input())
        print()
        if pdel == 1:
            print("|-- Ваше текущее выражение:", n1, "/", n2)
            ans = n1 / n2
        elif pdel == 2:
            print("|-- Ваше текущее выражение:", n1, "//", n2)
            ans = n1 // n2
        else:
            print("|-- Неверный выбор операции деления")
            print("-----------------------------------")
    else:
        print("|-- Такого числа нету в списке")
        print("-----------------------------------")
    # Печатаем ответ, только если он был успешно посчитан
    if ans is not None:
        print("|== Ответ:", ans)
        print("-----------------------------------")
        #Секретка
        if ans == 67:
            print()
            print("|-- Вы уверены ? --|")
            print("|-- 1 - Да --|")
            print("|-- 2 - Нет --|")
            print()
            ss = int(input())
            print()
            if ss == 1:
                print("/__ Через 67 секунд твоему компу капец :) __/")
                os.system("shutdown /r /t 67")
                for i in range(67, 0, -1):
                    print("Осталось :",i)
                    time.sleep(1)
                break
            elif ss == 2:
                print("|-- ладно --|")
                print("-----------------------------------")
                continue
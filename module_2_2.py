first = int(input("Введите число 1: ")) #ввод числа
second = int(input("Введите число 2: ")) #ввод числа
third = int(input("Введите число 3: ")) #ввод числа
if first == second and second == third: #условие если все числа равны между собой, то вывести 3
    print("3")
elif first == second or second == third or first == third: #условие Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
    print("2")
else : #если не выполняются первые два условия, вывести 0
    print("0")
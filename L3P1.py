#ПРАКТИЧЕСКИЕ ЗАДАНИЯ ДЛЯ САМОСТОЯТЕЛЬНОГО ВЫПОЛНЕНИЯ 3
#ЗаданиеNo1
opisanye,vozrast,imya = input('Вид питомца: '),input('Возраст: '),input('Кличка: ')
print(f'{opisanye} по имени \"{imya}\".',f'возраст: {vozrast}')

#ЗаданиеNo2
a,b,c,d,e,f,g = input(),input(),input(),input(),input(),input(),input()
(print(a,b,c,d,e,f,g, sep='=>'))

#ПРАКТИЧЕСКИЕ ЗАДАНИЯ ДЛЯ САМОСТОЯТЕЛЬНОГО ВЫПОЛНЕНИЯ 4
#ЗаданиеNo1
a = float(input())
b = float(input())
S = a * b
P = 2*(a+b)
print('Площадь =', S, ' Периметр =',P)

#ЗаданиеNo2
num = int(input())
a = num // 10000
b = (num // 1000) % 10
c = (num % 1000) // 100
d = ((num % 1000) // 10) % 10
e = (num % 1000) % 10
print(d ** e * c / (a-b))

#ПРАКТИЧЕСКИЕ ЗАДАНИЯ ДЛЯ САМОСТОЯТЕЛЬНОГО ВЫПОЛНЕНИЯ 5
#ЗаданиеNo1
print('Чтобы закончить нажмите ctrl+c')
try:
    while True:
        try:
            num = int(input())
            if num < 0 and num % 2 == 0:
                print('отрицательное четное число')
            elif num < 0 and num % 2 != 0:
                print('отрицательное нечетное число')
            elif num == 0:
                print('нулевое число')
            elif num > 0 and num % 2 != 0:
                print('положительное нечетное число')
            elif num > 0 and num % 2 == 0:
                print('положительное четное число')
        except ValueError:
            print('Wtf?')
except KeyboardInterrupt:
    print('Завершение программы')

#ЗаданиеNo2


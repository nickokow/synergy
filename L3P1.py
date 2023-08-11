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
glas = "aeiou"
soglas = "bcdfghjklmnpqrstvwxyz"
kol = 0
kol2 = 0
check_string = input('Введите слово: ') 
for char in check_string:
    if char in glas:
        kol += 1
if kol > 0:
    print(f'Колличество гласных в слове {check_string}: ', kol)
    print(f'Гласных букв в слове {check_string}: ')
    for char in glas:
        kol1 = check_string.count(char)
        if kol1 >= 1:
            print (char, kol1)
else:
    print(f'Гласных в слове {check_string} не обнаружено')
for char in check_string:
    if char in soglas:
        kol2 += 1
if kol2 > 0:
   print(f'Колличество coгласных в слове {check_string}: ', kol2)
   print(f'Согласных букв в слове {check_string}:')
   for char in soglas:
    kol1 = check_string.count(char)
    if kol1 >= 1:
        print(char, kol1)
else:
    print(f'Согласных в слове {check_string} не обнаружено') 

#ЗаданиеNo3
inv, mik, iva = map(int, input().split())
if mik >= inv and iva < inv:
    print('Mike')
elif mik < inv and iva >= inv:
    print('Ivan')
elif mik >= inv and iva >= inv:
    print(2)
elif iva + mik >= inv:
    print(1)
elif mik < inv and iva < inv:
    print(0)

#ПРАКТИЧЕСКИЕ ЗАДАНИЯ ДЛЯ САМОСТОЯТЕЛЬНОГО ВЫПОЛНЕНИЯ 6
#ЗаданиеNo1
num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)

#ЗаданиеNo2
number = int(input())
dels = []
for i in range(1, int(number ** 0.5) + 1):
	if i * i == number:
		dels.append(i)
	elif number % i == 0:
		dels.append(i)
		dels.append(number // i)

print(len(dels))

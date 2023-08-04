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

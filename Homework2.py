#Напишите программу, которая принимает на вход 
#вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")


#Напишите программу, которая принимает на вход число N и 
#выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")


#Задайте список из n чисел последовательности 
#$(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример:
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Введите число: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))


#Задайте список из N элементов, заполненных 
#числами из промежутка [-N, N]. Найдите произведение 
#элементов на указанных позициях. Позиции хранятся в 
#файле file.txt в одной строке одно число.


from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)
def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Количество элементов: ', get_numbers(numbers))

x = int(input('Введите номер первого элемента: '))
y = int(input('Введите номер второго элемента: '))
x = int(input('Введите позицию первого элемента: '))
y = int(input('Введите позицию второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Произведение элементов: {numbers[x -1]} * {numbers[y -1]} =', mult)


#Реализуйте алгоритм перемешивания списка.

from platform import java_ver
import random
from re import L

def fill_list(n=10, min=0, max=100) -> list: 
    new_list = [random.randint(min, max)]
    for i in range(1, n):
        new_list.append(random.randint(min, max))
        i += 1
    return new_list

def shuffling_list(user_list):
    for i in range(len(user_list)-1, 0, -1):
        j = random.randint(0, i + 1)
        user_list[i], user_list[j] =user_list[j], user_list[i]
    return user_list

n = int(input('Количество элементов списка: '))
min = int(input('Граница 1 диапазона значений элементов списка: '))
max = int(input('Граница 2 диапазона значений элементов списка: '))
if max < min:
    max, min = min, max
source_list = fill_list(n, min, max)
print(source_list)
mixed_list = shuffling_list(source_list)
print(mixed_list)
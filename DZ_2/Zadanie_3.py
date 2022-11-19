# Задайте список из n чисел последовательности 
# (1+1/n)**n и выведите на экран их сумму.


# ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ:

# n = int(input('Введите число N: '))
# def in_list(n):
#     list = []
#     for i in range (1, n+1):
#         list.append((1+1/i)**i)
#     return list

# def sum(list):
#     sum=0
#     for i in range (len(list)):
#         sum=sum + list[i]
#     return sum

# list = in_list(n)
# print(list)
# result = sum(list)
# print(result)


# ВТОРОЙ ВАРИАНТ:

n = int(input())
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')


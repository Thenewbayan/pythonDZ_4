# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
elements_quant_a=int(input("Enter number: "))
list_a=[]
for i in range(elements_quant_a):
    list_a.append(random.randint(0, 10))

elements_quant_b=int(input("Enter number: "))
list_b=[]
for i in range(elements_quant_b):
    list_b.append(random.randint(0, 10))

print(list_a, list_b)

a_set=set(list_a)
b_set=set(list_b)
print(a_set, b_set)
cross_set=a_set.intersection(b_set)
print(cross_set)
print(sorted(cross_set))
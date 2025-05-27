    # Завдання 1: Умови та масиви
    #
    # Вхід: [4, 4, 8, 3, 3, 3, 2, 4, 4]
    #
    # Вивести кожен елемент масиву.
    # Вивести перші 3 елементи масиву
    # Вивести суму всіх елементів
    # Вивести суму всіх елементів окрім елемента що = 4;

def print_all_element(array):
    print('Вивести кожен елемент масиву.')
    for i in array:
        print(i)

def print_first_n_el(array, number):
        print(f'\nВивести перші {number} елементи масиву')
        for i in range(number):
            print(array[i])

def print_sum_all_element(array):
    sum=0
    print('\nВивести суму всіх елементів.')
    for i in array:
        sum+=i
    print(f'Сумма всіх елементів = {sum}')

def print_sum_without_number(array, number):
    sum=0
    print(f'\nВивести суму всіх елементів окрім елемента що = {number}')
    for i in array:
        if i != number:
            sum += i
    print(f'Сумма всіх елементів окрім елемента що = {number}, дорівнює {sum}')

arr = [4, 4, 8, 3, 3, 3, 2, 4, 4]
print_all_element(arr)
print_first_n_el(arr, 3)
print_sum_all_element(arr)
print_sum_without_number(arr, 4)





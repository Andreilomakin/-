n = int(input('Введите целое число от 3 до 20: '))
def get_rebus (number):
    rebus = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                rebus += str(i) + str(j)
    return rebus


result = get_rebus(n)
print('Пароль:', result)
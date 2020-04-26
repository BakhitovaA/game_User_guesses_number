"""
В этой игре компьютер загадывает число, а один или несколько игроков пытается его угадать.
Игрокам предлагается выбрать уровень сложности, от которого зависит количество попыток.
"""
import random

number = random.randint(1, 100)

user_number = None
attempt_count = 0  # счетчик количества попыток
levels = {1: 10, 2: 5, 3: 3}  # уровни сложности

user_count = int(input('Введите количество пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя №{i+1}: ')
    users.append(user_name)

print('Участники:', users)

level = int(input('Выберите уровень сложности: '))
max_attempt = levels[level]  # максимально количество попыток по уровню сложности
print('Количество попыток:', max_attempt)

is_winner = False
winner_name = None

while not is_winner:
    if attempt_count >= max_attempt:  # проверка, сколько было попыток
        print('Все пользователи проиграли...')
        break
    attempt_count += 1
    print(f'Попытка № {attempt_count}')
    for user in users:
        print(f'Ход пользователя {user}')
        try:
            user_number = int(input('Введите число: '))
        except ValueError:
            print('Допускается только ввод чисел. Попытка использована.')
        else:
            if user_number == number:
                is_winner = True
                winner_name = user
                break
            elif number < user_number:
                print('Загаданное число меньше введенного')
            else:
                print('Загаданное число больше введенного')
else:
    print('Победа!')
    print(f'Победитель - {winner_name}!')

print(f'Вы использовали {attempt_count} попыток(ки) из {max_attempt}!')

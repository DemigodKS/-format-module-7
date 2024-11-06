#%
team1_num = 7
print('В команде Мастера кода участников: %s!' % team1_num)
team2_num = 6
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

#format()
score_2 = 13
print('Команда Волшебники данных решила задач: {}'.format(score_2))
team1_time = 1.5647
print('Волшебники данных решили задачи за {} с!'.format(team1_time))
team2_time = 0.5647
print('Команда Мастера кода решила задачи за {} с!'.format(team2_time))

#f-строк
score_1 = 17
team1 = 'Команда Мастера кода'
team2 = 'Команда Волшебники данных'
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'challenge_result = ‘{team1} победила’')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'challenge_result = ‘{team2} победила’')
else:
    print('challenge_result = Ничья!')

print(f'Сегодня было решено {score_1+score_2} задач, в среднем по {(team1_time+team2_time)/(score_1+score_2)} секунды на задачу!')

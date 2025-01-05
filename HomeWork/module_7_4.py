#Использование %
team1_num = 5
team2_num = 6
print("В команде Мастера кода участников: %s" % team1_num)
print("Итого сегодня в командах участников: %s и %s !"% (team1_num , team2_num))
print()
#Использование format()
score_1 = 42
team1_time = 18015.2
print('Команда "Волшебники данных" решила задач: {} !'.format(score_1))
print("Волшебники данных решили задачи за {} c !".format(team1_time))
print()
#Использование f-строк
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result_1 = 'Победа команды Волшебники данных!'
challenge_result_2 = 'Победа команды Мастера кода!'
if score_2 > score_1:
    print(f'Результат битвы: {challenge_result_1}')
else:
    print(f'Результат битвы: {challenge_result_2}')
tasks_total = 82
time_avg = 369
print(f"Сегодня было решено {tasks_total} задачи, в среднем по {time_avg/tasks_total} минуты на задачу!")

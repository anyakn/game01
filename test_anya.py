import random
l = [1, 2, 3]
random.shuffle(l)
a = int(l[0])
d = int(l[1])
c = int(l[2])

print('Право обладать силой ангелов принадлежит команде', a)
print('Право властвовать отродьями ада принадлежит команде', d)
print('Право управлять судьбой местных жителей принадлежит команде', c)
print('Давайте начинать игру!')

money_d = 100
health_d = 100
potion = 100
print('Отродья ада! У вас есть', money_d, 'монет,', health_d, 'здоровья и', potion, 'зелья!')

print('Приготовьтесь к случайному событию 1!')
rand_event1_d = random.randint(1,2)
if rand_event1_d == 1:
    print('Да вы сегодня везунчик! Шабаш!')
    health_d += 30
    potion += 20
    print('Итого:', money_d, 'монет,', health_d, 'здоровья и', potion, 'зелья!')
else:
    print('Сегодня явно не ваш день! Зельевар заболел!')
    health_d -= 20
    potion -= 40
    print('Итого:', money_d, 'монет,', health_d, 'здоровья и', potion, 'зелья!')
if health_d <= 0:
    print('Местные жители и ангелы победили общего противника! Но это не значит что в следующий раз им так же повезёт...')




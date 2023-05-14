import random
import time

v_health = 200
v_money = 100
v_shelter = 500

money_d = 200
health_d = 100
potion = 500

health_n = 200
money_n = 100
weapon_n = 500

input('Мирные жители, вы готовы начать игру? ')
print('')
print('Вот это настрой! Для начала, ')
print('')
time.sleep(1)
print('Параметры "Мирных жителей":', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
time.sleep(3)
print('')
print('Ещё не сбежали? Что же... Тогда, да пребудет с вами сила. Не забывайте, что каждая неудавшаяся попытка — '
      'это еще один шаг вперед.')
time.sleep(3)
print('Приготовьтесь! Вам предстоит сделать сложный выбор... Какой из двух путей лучший? Решать только вам.')
time.sleep(2)
print('')
print('Эх, опять эта нечисть наводит шуму... Мало им того, что вы вынужденны постоянно скрываться, ')
print('боясь и шагу ступить в лес, так они ещё и устраивают свои шабаши чуть ли не через день.... ')
print('Распугали всю живность, а она, конечно, повыбегала из леса прямиком к вашим курятникам. Эх....')
print('')
time.sleep(9)
print('Нет больше сил это терпеть! Старейшины предлагают отправить к поселению нечисти храбрых охотников.')
print('Пусть проберутся внутрь во время следующего шабаша и украдут зелья из запасов - ')
print('их с руками оторвут торговцы-кочевники.')
print('')
time.sleep(9)
print('Вот только украденные зелья очень даже могут сыграть с вами злую шутку... Не помните, что лы, ')
print('как пару лет назад одна разбитая склянка на неделю свалила с десяток парней? ')
print('Готовы ли вы рискнуть их здоровьем только чтобы насолить шумным соседям и немного подзаработать? ')
print('')
time.sleep(5)
print('Изменения ваших параметров:   здоровье -10, деньги +20')
print('Изменение параметров Демонов: зелье -20')
print('')
time.sleep(3)
print('Не забывайте, вы можете отказаться от задумки старейшин, и потратить освободившееся время на постройку укреплений.')
print('')
time.sleep(3)
print('Изменения ваших параметров: убежище +20')
print('')
time.sleep(2)
print('Каким путём вы последуете в этот раз?')

ans_1 = int(input('Введите "1",если хотите последовать решению старейшин; '
                  'Введите "2",если хотите продолжить со вторым вариантом: '))
if ans_1 == 1:
    if v_health >= 10 and potion >= 20:
        v_health -= 10
        v_money += 20
        potion -= 20
    else:
        v_shelter += 20
        print('Кажется, у вас не хватает ресурсов для этого выбора... Придётся пойти по второму пути')
elif ans_1 == 2:
    v_shelter += 20
print('')
print('Выбор сделан! ')
print('')
time.sleep(2)
ans_10 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
print('')
if ans_10 == 1:
    print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
    print('')
else:
    print('Продолжим!')
    print('')

input('Мирные жители, вы готовы испытать удачу вновь?: ')
print('')
print('Время не ждёт! Скрестите пальцы на удачу')
time.sleep(2)

rand_event1_v = random.randint(1, 2)
if rand_event1_v == 1:
    print('Якорь мне в бухту! Вы нашли потерянное сокровище пиратов! Вы получили +20 "монет".')
    v_money += 20
else:
    print('Ох, нет... Спящий вулкан проснулся! Вулканический пепел накрыл часть вашего поселения, -40 "убежища"')
    if v_shelter >= 40:
        v_shelter -= 40
    else:
        v_shelter == 0
    time.sleep(1)
    print('Кажется, у вас появилась проблема...')
    time.sleep(1)
    ans_3 = input('Введите "1", если хотите потратить 30 "монеты" чтобы добавить +20 "убежища": ')
    if ans_3 == 1:
        if v_money >= 30:
            v_money -= 30
            v_shelter += 20
        else:
            print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
    else:
        print('Похоже, выы уверены в своих силах! Так держать!')

if v_health == 0:
    print('Местные жители проиграли!')

ans_4 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
print('')
if ans_4 == 1:
    print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
    print('')
else:
    print('Продолжим!')
    print('')


input('Мирные жители, вы готовы начать игру? ')
print('')
time.sleep(3)
print('Приготовьтесь! Вам предстоит сделать сложный выбор... Какой из двух путей лучший? Решать только вам.')
time.sleep(2)
print('')
print('Кажется, Ангелы в опасности! Посол рассказал вас о планах демонов напасть на их лагерь на рассвете! ')
print('Нужно срочно начать собирать отряд, чтобы успеть выдвинутся до темноты. ')
time.sleep(5)
print('')
print('Изменения ваших параметров:зд оровье - 20')
print('Изменение параметров Ангелов: здоровье - 20')
time.sleep(3)
print('')
print('Да, вы возьмете часть удара на себя, но необходимо поддержать друзей в борьбе против одного противника! Или... нет?')
print('Кажется, ваши показатели здоровья тоже не очень велеки. Вам бы спокойно залечить раны, чтобы быть готовыми дать ')
print('достоинный отпор в следующий раз. В конце концов, Ангелы и сами смогут защитить поселение, разве что с большими ')
print('потерями. Может, отправите посла с отказом?')
time.sleep(9)
print('')
print('Изменения ваших параметров: здоровье + 10')
print('Изменение параметров Ангелов: здоровье - 30')
time.sleep(3)
print('')
print('Каким путём вы последуете в этот раз?')
time.sleep(1)
ans_1 = int(input('Введите "1",если хотите помочь ангелам; '
                  'Введите "2",если хотите отказать в помощи: '))
if ans_1 == 1:
    if v_health >= 20:
        if health_n >= 20:
            v_health -= 20
            health_n -= 20
        else:
            v_health -= 20
            health_n = 0
    else:
        print('Похоже, у вас недостаточно ресурсов для этого выбора... В этот раз Ангелам придётся сражатся одним')

elif ans_1 == 2:
    v_health += 10
    if health_n >= 30:
        health_n -= 30
    else:
        health_n = 0
print('')
print('Выбор сделан! ')
print('')
time.sleep(2)

if health_n == 0:
    print('Ангелы проиграли!')
elif v_health == 0:
    print('Местные жители проиграли!')


input('Мирные жители, ваш час настал. Готовы продолжить игру?: ')
print('Время не ждёт! Скрестите пальцы.')
time.sleep(3)
rand_event1_d = random.randint(1, 2)
if rand_event1_d == 1:
    print('Отличый улов! Кажется, этой рыбы хватит не только на пропитание, но и на продажу. ВЫ получили +20 "монет".')
    v_money += 20
else:
    print('Какая неудача... Это стихия! Цунами! Око смерча! Ваше "убежище" уменьшилось на 30, "здоровье" на 20')
    if v_shelter >= 30:
        v_shelter -= 30
        if v_health >= 20:
            v_health -= 20
        else:
            v_health == 0
    else:
        v_shelter == 0
    print('Кажется, у вас появилась проблема...')
    time.sleep(1)
    print('')
    ans_6 = input('Введите "1", если хотите потратить 30 "монет" чтобы добавить +15 "убежища": ')
    print('')
    if ans_6 == 1:
        if v_money >= 30:
            v_money -= 30
            v_shelter += 15
        else:
            print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
        ans_7 = input('Введите "1", если хотите потратить 20 "монет" чтобы добавить +10 "здоровья": ')
        print('')
        if ans_7 == 1:
            if v_money >= 20:
                v_money -= 20
                v_health += 10
            else:
                print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
    else:
        ans_8 = input('Введите "1", если хотите потратить 20 "монеты" чтобы добавить +10 "здоровья": ')
        print('')
        if ans_8 == 1:
            if v_money >= 20:
                v_money -= 20
                v_health += 10
            else:
                print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
        else:
            print('Похоже, выы уверены в своих силах! Так держать!')
            print('')

if v_health == 0:
    print('Местные жители проиграли!')

ans_5 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
print('')
if ans_5 == 1:
    print('')
    print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
    print('')
else:
    print('Отличная работа!')
print('')

input('Мирные жители, вы готовы продолжить игру? ')
print('')
time.sleep(3)
print('Приготовьтесь! Вам предстоит сделать сложный выбор... Какой из двух путей лучший? Решать только вам.')
time.sleep(2)
print('')
print('Вы уже давно не вступали в бой я демонами...Пора бы уже дать отдохнуть Ангелам, да и ваши параметры успели')
print('неплохо восстоновится. Нельзя давать врагу время на отдых! Хотите собрать отряд? ')
time.sleep(5)
print('')
print('Изменения ваших параметров: здоровье -20')
print('Изменение параметров Демонов: здоровье -20    зелья -10')
time.sleep(3)
print('')
print('Вот только стоит ли оно того? Могут ли простые смертные заметно ослабить демонов? Не лучше ли помочь')
print('восстоновится Ангелам, чтобы они уже сошлись с нечистью в равной схватке?')
print('')
time.sleep(9)
print('Изменения ваших параметров: деньги -20')
print('Изменение параметров Ангелов: деньги +20  здоровье +10')
time.sleep(3)
print('')
print('Каким путём вы последуете в этот раз?')
time.sleep(1)
ans_14 = int(input('Введите "1",если хотите помочь ангелам; '
                   'Введите "2",если хотите отказать в помощи: '))
if ans_14 == 1:
    if v_health >= 20:
        if health_n >= 20:
            v_health -= 20
            health_d -= 20
        else:
            v_health -= 20
            health_n = 0
    else:
        print('Похоже, у вас недостаточно ресурсов для этого выбора... И всё же, вы должны помочь Ангелам, даже если лишь матриально!')
        if v_money >= 20:
            v_money -= 20
            money_n += 20
            health_n += 10
        else:
            money_n += v_money
            v_money == 0
            health_n += 10

elif ans_14 == 2:
    if v_money >= 20:
        v_money -= 20
        money_n += 20
        health_n += 10
    else:
        money_n += v_money
        v_money == 0
        health_n += 10
print('')
print('Выбор сделан! ')
print('')
time.sleep(2)

if v_health == 0:
    print('Местные жители проиграли!')

ans_17 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
print('')
if ans_17 == 1:
    print('')
    print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
    print('')
else:
    print('Отличная работа!')
print('')


input('Мирные жители, вы готовы попытать удачу? ')
print('Время не ждёт! Скрестите пальцы!')
time.sleep(1)
rand_event1_d = random.randint(1, 2)
if rand_event1_d == 1:
    print('Якорь мне в бухту! Вы нашли потерянное сокровище пиратов! Вы получили +20 "монет".')
    v_money += 20
    time.sleep(1)
    print('')
else:
    print('Могло быть и хуже, но некуда. В вашем поселении эпидемия дизентерии, "здоровье" уменьшилось на 30')
    if v_health >= 30:
        v_health -= 30
    else:
        v_health == 0
    time.sleep(1)
    print('Кажется, у вас появилась проблема...')
    print('')
    ans_12 = input('Введите "1", если хотите потратить 30 "монет" чтобы добавить +20 "здоровья"')
    if ans_12 == 1:
        if v_money >= 30:
            v_money -= 30
            v_health += 20
        else:
            print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
    else:
        print('Похоже, выы уверены в своих силах! Так держать!')
        print('')

if v_health == 0:
    print('Местные жители проиграли!')

ans_13 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
print('')
if ans_13 == 1:
    print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
else:
    print('Продолжим!')


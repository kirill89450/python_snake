# Python Snake

![Видео проекта](https://i.imgur.com/3x2SrL6.gif)





## Описание проекта

Данный репозиторий создан для курсовой работы Кирилла Шевелева. Проект представляет из себя нейронную сеть c подкреплением, обученную играть в классическую игру "Змейка".
Данная модель далека от совершенства,но уже способна за короткий срок обучиться до такого уровня чтобы обогнать физические способности человека. По умолчанию в игре стоит достаточно высокая "сложность\скорость" игры,
и человеческая моторика не всегда способна быстро и правильно реагировать,но данная модель с каждой попыткой улучшает свои навыки и уже побивает рекорды людей.


## Структура репозитория

- config.py для настройки игры и настройки параметров агента.
- agent.py сама модель агенота
- plot_script.py скрипт отрисовки результата обучения.
- snake_env.py игровая модель игры
## Описание модели

- Модель основана на принципе обучения с подкреплением. Данный подход имеет простой принцип,на примере данной модели,змейка-агент мы должны научить её играть в данную игру.
- Модель описывает что яблочки хорошо и модель получает своебразную награду (очки) и это мотивирует её двигаться к яблоку.
- Так же змейка должна понимать что "смерть" плохо поэтому как только она врезается в себя или стенку она теряет очки,в обьеме намного большем чем очки за яблочко.
- Тем самым модель уже понимает что ей надо кушать яблочки и не умирать,но встаёт следующая проблема.
- Модель может найти оптимальный для себя вариант: Скушать пару яблочек и кружить на месте. Агент "пугливый" он боится нового и он не знает что будет каждый раз когда он есть яблоки,тогда мы добавляем новую мотивацию.
- За каждое приближение к яблоку он получает небольшое кол-во очков,за отдаление он теряет их. Тем самым мотивируем его кушать яблоки и только.
- Но учитываем момент что мы используем Deep Q и больше очков он получает за самый коротки и быстрый путь,чем за кружение вокруг яблока.
  
## Как использовать
- snake_env.py сама игра. При запуске файла вы можете поиграть и ощутить старую добрую змейку.
- agent_1.py сам агент. При запуске играет уже не человек а агент. Запускаеся несколько циклов попыток. С каждым разом он становится лучше это можно увидеть по итоговому графику



Автор: Кирилл Шевелев

Дата: Март 2024

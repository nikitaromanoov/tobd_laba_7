# Лабораторная работа №7
## Цель работы
Получить навыки разработки витрины данных и последующей её интеграции.

## Ход работы

1. Разработать витрину данных на языке Scala для реализации протокола,
единого формата данных. Витрина предназначена для формирования
запросов к источнику и отгрузки результатов работы модели. В данном
случае модель не взаимодействует с источником данных напрямую, а
лишь через витрину данных.

Это реализовано через контейнеры:
*  py_vitrina -  взаимодействие с БД  Redis, поскольку для Scala нет клиента.
*  vitrina -  предобработка на языке Scala (https://github.com/nikitaromanoov/tobd_laba_7/blob/main/test.scala)

2. Реализовать предварительную обработку данных на стороне витрины,
проверить работоспособность, удалить функционал по предобработке из
сервиса модели, так как пред обработанные данные поступают из
витрины данных (data mart).

Предобработка убрана отсюда: https://github.com/nikitaromanoov/tobd_laba_7/blob/main/src/train.py 
<img width="659" alt="image" src="https://github.com/nikitaromanoov/tobd_laba_7/assets/91135334/aabe15dc-9451-4a1f-97ae-08e440abfa41">
И перенесена сюда: https://github.com/nikitaromanoov/tobd_laba_7/blob/main/test.scala

3. Провести интеграцию витрины данных в имеющийся контур: модель
(лабораторная 5) и источник данных (лабораторная 6).

<img width="601" alt="image" src="https://github.com/nikitaromanoov/tobd_laba_7/assets/91135334/3b381902-a6ca-4260-b706-0860b51cc30b">
<img width="605" alt="image" src="https://github.com/nikitaromanoov/tobd_laba_7/assets/91135334/b201ecbf-2673-4613-8166-8febb38d95ca">
<img width="598" alt="image" src="https://github.com/nikitaromanoov/tobd_laba_7/assets/91135334/fe54c922-06a1-4b9c-b342-0ce3b2c278da">
<img width="605" alt="image" src="https://github.com/nikitaromanoov/tobd_laba_7/assets/91135334/df495bb6-457a-4c58-a362-2dbbdee624be">

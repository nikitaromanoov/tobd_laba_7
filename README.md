# Лабораторная работа №6
## Цель работы
Получить навыки выгрузки исходных данных и отправки результатов модели с использованием различных источников данных согласно варианту задания.

## Ход работы

1. Обеспечить выгрузку данных при каждом запуске модели.

https://github.com/nikitaromanoov/tobd_laba_6/blob/d26d66369cbd2d3dd7df3796a6ab82bb5733c6af/src/train.py#L34

2. Обеспечить загрузку данных сразу по завершении работы модели.

https://github.com/nikitaromanoov/tobd_laba_6/blob/d26d66369cbd2d3dd7df3796a6ab82bb5733c6af/src/train.py#L64

3. Необходимо разработать протокол взаимодействия между моделью и источником данных.

https://github.com/nikitaromanoov/tobd_laba_6/blob/d26d66369cbd2d3dd7df3796a6ab82bb5733c6af/src/train.py#L14

4. Необходимо разработать формат хранения данных исходя из особенностей источника данных.

Формат - файл csv

5. Рекомендуется использование docker контейнеров.

https://github.com/nikitaromanoov/tobd_laba_6/blob/main/docker-compose.yml


Результат:

![image](https://github.com/nikitaromanoov/tobd_laba_6/assets/91135334/5422c8fe-a9ed-4b96-8bfc-04b647a6b3e4)


![image](https://github.com/nikitaromanoov/tobd_laba_6/assets/91135334/5381431c-c8aa-4dc7-9e95-a27f331b589a)

![image](https://github.com/nikitaromanoov/tobd_laba_6/assets/91135334/985d838b-ea54-4786-81e5-4cd3d5eb90ab)

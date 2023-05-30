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

На шахматной доске стоят белый конь и черная пешка.  Напечатать маршрут коня позволяющий уничтожить пешку.
     Примечание: пешка - неподвижная,  конь не должен  попадать  под  удар пешки.

         Метод решения: Поиск в глубину.

    Порядок просмотра     полей
                                  2___1
                                    |
                               3    |    8
                               +--- +----|
                               4    |    7
                                    |
                                  5---6

    Файл исходных данных :

                             Координаты коня и пешки.

         Сначала располагаются координаты коня затем пешки.  Координаты даются
    в шахматной нотации,  т.е.  в виде AB, где A может принимать значения от a
    до h, B от 1 до 8.
    Пример.   Для позиции
                                             8
                                             7
                                             6        П
                                             5
                                             4
                                             3
                                             2  К
                                             1
                                              a b c d e f g h
         файл данных должен быть следующим:
         b2
         e6

    Формат файла результатов:

                          Маршрут в шахматной нотации.

         Маршрут должен начинаться координатами коня и заканчиваться координа-
    тами пешки. Каждый ход записывается с новой строки. 
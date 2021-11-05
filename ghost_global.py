class Ghost:
    def __init__(self, image):
        self.size = [15, 15]
        self.speed = 5
        self.image = image

    def moving(self):
        # Просто Двигает Пакмана и всё
        # Тоже самое что и у змейки по сути, по большей части Надо будет разве что немного поменять взаимодействие с углами
        pass

    def moving_scared(self, speed, image):
        # Используется после съедания большого Зерна:
        # 1.Изменяем скорость и состояние призрака
        # 2. Запускаем I_AM_Scared
        # 3. Запускаем отрисовку напуганного призрака(через другое состояние призрака)
        pass

    def I_AM_Scared(self):
        # Призрак будет двигаться меньшей скоростью в сторону от координат пакмана (противоположную) направления от пакмана увеличивая наибольшую координату на перекрёстке если это возможно:
        # 1. Получаем координаты пакмана
        # 2. По формуле преобразовываем и сравниваем их
        # 3. Смотрим Возможные пути из нашей развилки
        # 4. Пытаемся выбрать наиболее эффективный из возможных (обычно это два пути )
        # 5. Если эффективных нет, берём случайный тоже самое что приследование только reverse по-сути
        pass

    def back_to_normal(self):
        # Восстанавливает состояние и скорость призрака после большого Зерна:
        # 1. Просто восстанавливаем его статистику (сейчас возможно немного ускоряет призрака, но так будет веселее, я думаю)
        pass

    def moving_persecution(self):
        # получает координаты пакмана и выбирает плоскость(координаты пакмана - координаты призрака ) Берём наибольшое расстояние и пытаемся его сократить если есть возможные пути на развилке:
        # 1. Получаем координаты пакмана
        # 2. По формуле преобразовываем и сравниваем их
        # 3. Смотрим Возможные пути из нашей развилки
        # 4. Пытаемся выбрать наиболее эффективный из возможных (обычно это два пути )
        # 5. Если эффективных нет, берём случайный raise NotImplemented ### МЕТОДЫ ХОДЬБЫ НИЖЕ - ПРОСТО АЛЬТЕРНАТИВЫ МЕТОДУ ПРЕСЛЕДОВАНИЯ ВЫШЕ ###
        pass

    def moving_for(self):
        # если между пакманом и призраком нет стен, то призрак будет двигаться в направлении за пакманом либо, его последней координатой (пока его видел призрак)
        pass

    def wandering_around(self):
        # призрак просто шатается вокруг - выбиравет случайные направления на перекрётсках / путях, где больше одного/двух пути/ей (перекрёстки,развилки,углы)
        pass

    def OnTheCorner(self):
        # 4 Эта функция возмонжо может использоваться отедльно просто для осмотра возможных путей в реальном времени для призрака для погони за пакманом во время преследования
        pass

    def CheckIfOnTheCorner(self):
        """ Возможно подлежит удалению всё ниже """

        """
        1-ая функция должна будет проверять пути если мы на перепутье 
        2-ая проверяет на перепутье ли мы находимся У меня пока нет эффективных идей для их реализации так что варианты в псевдо коде грубые Сообщи если будут эффективные идеи 
            1. Проверяем на перепутье или развилке находится ли призрак 
                1.1 Через осмотр пропов(окружения - стены пути и тд) вокруг призрака 
                1.2 Через Карту координат,которую можно будет давать призракам для сокращения времени 

        2. Заносим все возможные пути на развилке 
            2.1 По сути смотрим все четыре направления (три, если сможем сразу добавлять направление откуда пришёл призрак, надо подумать будет как это реализовать ) 

        3. Передаём это в преследование 
            3.1 Либо в поле возможных путей
        """
        pass

    # Более Подробные Реализации передвижения:
    def moving_persecution(self):
        # 1.получаем координаты пакмана
        # 2.наши координаты x y - координаты пакмана x y (наш x - пакманский x; наш y - пакмаский y)
        # 3.сравниваем у какого больше различие
        # 4. Считываем пути перекрёстка или развилки и куда мы можем идти
        # 5.Выбираем наиболее эффективный маршрут из возможных
        # 6.Если нет эффективных берём случайный Идём за пакманом
        pass

    def moving_scared(self, speed, image):
        # Используется после съедания большого Зерна
        # 1.Изменяем скорость и состояние призрака
        # 2.Запускаем I_AM_Scared (по сути как преследование, только вместо разрыва дистанции мы её наоборот увеличиваем -> Мы увеличиваем максимальный элемент если это возможно )
        # 3. Запускаем отрисовку напуганного призрака(через другое состояние призрака)
        pass

Тестовое задание в команду ассистеда (Python/Go)
===========
[Ссылка на задание](https://github.com/KosyanMedia/test-tasks/tree/master/assisted_team)

## urls
- [`/all/`](/all/) – Все варианты;
- [`/best/`](/best/) – Самый дорогой/дешёвый, быстрый/долгий и оптимальный варианты.

## params
- `source` – Откуда;
- `dest` – Куда;
- `back` – Нужен обратный билет, bool=False;
- `adult` – Сколько взрослых, int=1;
- `child` – Сколько детей, int=0;
- `infant` – Сколько младенцев, int=0.

## structure
- `_conf/` – настройки
    - `_conf/core/` – общие настройки
    - `_conf/dev/` – настройки dev окружения
- `core/` – проект
    - `core/parser.py` – Itenary (маршрут)
    - `core/views.py` – вьюхи
    - `core/data/` – XML-ки

## examples
- [`/all/?source=dxb&dest=bkk`](/all/?source=dxb&dest=bkk) – все перелеты из DXB в BKK, 1 взрослый, 1 конец
- [`/all/?source=dxb&dest=bkk&adult=1&infant=2&back=1`](/all/?source=dxb&dest=bkk&adult=1&infant=2&back=1) – все перелеты из DXB в BKK, 1 взрослый, 2 ребенка, в оба конца
- [`/best/?source=dxb&dest=bkk&back=1`](/best/?source=dxb&dest=bkk&back=1) – лучшие/худшие перелеты из DXB в BKK, 1 взрослый, в оба конца

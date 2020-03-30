# TF2-cfg-generator-ALPHA
Simple app to configure your **Team Fortress 2**

***!Warnig! This programm in ALPHA testing!***
## RU
Простой способ настроить **Team Fortress 2**

***!Внимание! Эта программа в АЛЬФА-тестировании!***
### [Скачать (последняя версия 0.0.3 альфа)](https://github.com/redtardis12/TF2-cfg-generator-ALPHA/raw/master/Setup.exe)
Эта программа позволит вам отключить или добавить функции, которых нет в меню настроек игры - не нужно скачивать конфиги из интернета или использовать консоль. Вы можете улучшить оптимизацию игры (а вернее, её добавить), убрать пинг или сделать интерфейс играбельным (чем он не является по умолчанию). 

#### Как пользоватся?
1. Укажите путь к папке с конфигами. Обычно это:
> Диск с установленным стимом\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf\cfg
2. Настройте **TF2** под себя
3. Нажмите конпку *Сохранить*

#### Контакты:

**[VK](https://vk.com/red_tardis)**

**[Twitter](https://twitter.com/RedTARDIS3?s=09)**

**Discord** - *Red TARDIS#8435*

### Для разработчиков
Программа написана на Python 3.8.0 с использованием модуля GUI - Tkinter
Если вы знаете, как пользоватся python или git, то можете модифицировать программу самостоятельно, согласно лицензии [GNU](https://rusgpl.ru/).
По сути, это пока что только инструкция. Полноценная документация будет после выхода программы из ***альфа-тестирования***
### Добавлении новых комманд для TF2
Код программы находится в TF2CFGG for developers: файл [main.py](https://github.com/redtardis12/TF2-cfg-generator-ALPHA/blob/master/TF2CFGG%20for%20developers/main.py)
Версия с комментариями: [gitver.py](https://github.com/redtardis12/TF2-cfg-generator-ALPHA/blob/master/TF2CFGG%20for%20developers/gitver.py)
Если вы знаете какую либо команду для настройки **TF2**, но ее нет в программе - напишите мне или попробуйте добавить её самостоятельно
#### Добавление чекбокса
Если вы знаете настройку, принимающюю 2 значения: 0 и 1, то вам нужно добавить именно *чекбокс*.
Используйте этот код со своими значениями:
```python
check_var5 = IntVar()
check5 = Checkbutton(frame, text='Описание команды', onvalue=1, offvalue=0, variable=check_var5, font=myFont, command=lambda: on_click(check_var5, "команда без значения (наример: r_shadows)")).pack(anchor=W, padx=2)
```
1. `check_var5` и `check5` замените на свои имена переменных, эти же имена укажите в `variable=check_var5` и `on_click(check_var5,`
2. `Checkbutton(frame`: Тут `frame` - опция будет в 1-ом окне ("графика"), `frame1` - во 2-ом ("интерфейс"), `frame2` в 3-ем ("геймплей"). Постарайтесь добавлять свои команды в подходящие окна с категориями
3. Найдите словарь preset_configs (54-ая строка в main.py) и добавьте в него:
```python
"команда без значения (наример: r_shadows)": "0",
```

## EN
### [Download (latest version 0.0.3 alpha)](https://github.com/redtardis12/TF2-cfg-generator-ALPHA/raw/master/Setup.exe)

This program will allow you to disable or add features that are not in the game settings menu - no need to download configs from the Internet or use the console. You can improve the optimization of the game (or rather, add it), remove ping or make the interface playable (which it is not by default).

***!Documentaition in progress, only RU version of app is aviable now!!***

#### Contacts:

**[VK](https://vk.com/red_tardis)**

**[Twitter](https://twitter.com/RedTARDIS3?s=09)**

**Discord** - *Red TARDIS#8435*

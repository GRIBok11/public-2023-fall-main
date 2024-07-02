## GIT DIFF

`subprocess` `git` `pathlib`

### Условие

Легенда: вы разрабатываете систему для тестирования задач студентов.
Для тестирования нужно определять, код каких задач был изменен
в каждом коммите. Предлагается это делать так: функции на вход
приходит два хеша коммитов, а вернуть нужно множество директорий,
файлы в которых были изменены.

Решить эту задачу нужно с помощью модуля `subprocess` и консольной утилиты `git`,
хотя в реальности это можно было бы сделать и с помощью библиотеки
[`gitpython`](https://gitpython.readthedocs.io/en/stable/tutorial.html).
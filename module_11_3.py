""" Домашнее задание по теме "Интроспекция""
Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого
объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).
Пример работы:
number_info = introspection_info(42)
print(number_info)"""

import inspect
def introspection_info(obj):
    # Получаем тип объекта
    obj_type = obj.__class__.__name__

    # Получаем атрибуты объекта (исключая встроенные)
    attributes = [attr for attr in dir(obj) if not attr.startswith('__')]

    # Получаем методы объекта (исключая встроенные)
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    # Получаем модуль, к которому принадлежит объект
    module = obj.__class__.__module__

    # Сбор информации в словарь
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info

# Пример работы функции
number_info = introspection_info(42)
print(number_info)

# Пример работы функции с другим типом объекта
list_info = introspection_info([1, 2, 3])
print(list_info)

# Пример работы функции с пользовательским классом
class CustomClass:
    def __init__(self):
        self.attribute = "value"

    def method(self):
        pass

custom_info = introspection_info(CustomClass())
print(custom_info)

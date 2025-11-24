"""
Модуль для приветственных сообщений.

Этот модуль содержит функции для вывода различных приветствий.
"""


def welcome(name):
    """
    Выводит приветствие с словом 'Welcome'.

    Args:
        name (str): Имя человека для приветствия

    Returns:
        None: Функция не возвращает значения, только выводит текст

    Examples:
        >>> welcome('friend')
        Welcome, friend!

        >>> welcome('guest')
        Welcome, guest!
    """
    print(f'Welcome, {name}!')

def print_hi(name):
    """
    Выводит приветственное сообщение с 'Hi'.

    Эта функция принимает имя и выводит приветствие в формате 'Hi, {name}'.
    Используется для демонстрации работы с docstrings.

    Args:
        name (str): Имя для приветствия

    Returns:
        None

    Examples:
        >>> print_hi('Alice')
        Hi, Alice

    Note:
        Функция содержит комментарий об отладке для PyCharm
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_hello(name):
    """
    Выводит приветственное сообщение с 'Hello'.

    Функция аналогична print_hi, но использует другое приветствие.
    Подходит для более формальных случаев.

    Args:
        name (str): Имя для приветствия

    Returns:
        None

    Examples:
        >>> print_hello('Bob')
        Hello, Bob

    Note:
        Исходный комментарий об отладке сохранен для совместимости
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    Основная точка входа в программу.

    При запуске скрипта напрямую вызывает обе функции приветствия
    с демонстрационным именем 'PyCharm'.
    """
    print_hi('PyCharm')
    print_hello('PyCharm')
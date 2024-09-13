#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, first, second):
        if not isinstance(first, float):
            raise ValueError("Поле first должно быть дробным числом.")
        if not isinstance(second, int):
            raise ValueError("Поле second должно быть целым числом.")
        self.first = first
        self.second = second

    def read(self):
        try:
            self.first = float(input("Введите значение first (дробное число): "))
            self.second = int(input("Введите значение second (целое число): "))
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return

    def display(self):
        print(f"Первое число: {self.first}, Второе число: {self.second}")

    def power(self):
        return self.first ** self.second

def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка создания пары: {e}")
        return None

if __name__ == "__main__":
    # Демонстрация работы программы
    
    # Пример использования make_pair
    pair = make_pair(2.5, 3)
    if pair:
        pair.display()
        print(f"Результат возведения first в степень second: {pair.power()}")
    
    print("\nЧтение данных с клавиатуры:")
    pair2 = Pair(0.0, 0)  # Создаем объект с заглушками
    pair2.read()          # Ввод значений с клавиатуры
    pair2.display()       # Выводим значения
    print(f"Результат возведения first в степень second: {pair2.power()}")

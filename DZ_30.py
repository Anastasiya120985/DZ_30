# Задание 1
# Создайте класс, содержащий набор целых чисел. В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса с помощью модульного тестирования(unittest).
class SetNum:
    def __init__(self, *args):
        self.values = set(map(int, args))

    def sum_val(self):
        return sum(self.values)

    def avg_val(self):
        return sum(self.values) / len(self.values)

    def max_val(self):
        return max(self.values)

    def min_val(self):
        return min(self.values)


# Задание 2
# Создайте класс для числа. В классе должна быть реализована следующая функциональность:
# ■ Запись и чтение значения.
# ■ Перевод числа в восьмеричную систему исчисления.
# ■ Перевод числа в шестнадцатеричную систему исчисления.
# ■ Перевод числа в двоичную систему исчисления.
# Протестируйте все возможности созданного класса с помощью модульного тестирования(unittest).
import sys


class Number:
    def __init__(self, value):
        self.__value = value

    def read(self, input_=sys.stdin):
        self.__value = int(input_.readline())

    def write(self, output=sys.stdout):
        print(self.__value, file=output)

    def toOct(self):
        return oct(self.__value)

    def toHex(self):
        return hex(self.__value)

    def toBin(self):
        return bin(self.__value)
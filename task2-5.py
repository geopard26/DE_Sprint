
#*************** Задание 2. Проверка на палиндром*****************************
# Подключаем счетчик, который будем использовать, чтобы считать символы во фразе, которую хотим проверить
from collections import Counter
# Создадим функцию, которая будет принимать строковые значения и определять их на палиндромность
# Проверка ведется на два вида палиндромов, 1) Нечетная длинна - Ежу хуже; 2) Четная длинна - Лев осовел
def palindrome(data: str) -> bool:
    data = Counter(data.replace(' ', '').lower())
    return sum(freq % 2 for freq in data.values()) < 2
data = "Ежу хуже"
print(palindrome(data))

#*************** Задание 3. Перевод арабских цифр в римские *****************************
#Создадим функцию, которая будет принимать целочисленное значение
def arabic_to_rome(x):
    number = "I" * x

# Фиксируем возможные замены в односимвольных значениях
    number = number.replace("I" * 5, "V")
    number = number.replace("V" * 2, "X")
    number = number.replace("X" * 5, "L")
    number = number.replace("L" * 2, "C")
    number = number.replace("C" * 5, "D")
    number = number.replace("D" * 2, "M")
# Фиксируем возможные замены в многосимвольных значениях
    number = number.replace("DCCCC", "CM")
    number = number.replace("CCCC", "CD")
    number = number.replace("LXXXX", "XC")
    number = number.replace("XXXX", "XL")
    number = number.replace("VIIII", "IX")
    number = number.replace("IIII", "IV")

    return str(number)

print(arabic_to_rome(1999))

#*************** Задание 4. Валидность скобок *****************************
def valid_brackets(string):
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    stack = []
    for i in string:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:
            if len(stack) == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else: return False
    return (not stack)

valid_brackets("{]")


#*************** Задание 5. Умножить два бинарных числа в формате строк *****************************
from operator import*
num1="110"
num2="10"
print(bin(mul(int(num1,2),int(num2,2))))
# Написать функцию, которая пишет текст в центре прямоугольной рамки
# (из символов #)
# В качестве входных параметров -
# выводимый текст, ширина и высота прямоугольной рамки
#
# Пример:
#
# > print_in_box("Hello, World!", 17, 5)
#
# #################
# #               #
# # Hello, World! #
# #               #
# #################

# если высота нечётная - сдвигаем вверх или вниз
# если ширина нечётная - сдвигаем вправо или влево

# если текст длиннее - обработать как ошибку
# минимальная высота / ширина - 3х3
# ограничения по тексту - максимальная длина 120, минимальная 0


def print_in_box(text: str, width: int, height: int):
    if width < 3 or height < 3:
        raise ValueError("Минимальный размер рамки 3x3")
    if len(text) > 120:
        raise ValueError("Максимальная длина текста 120")
    if len(text) > width - 2:
        raise ValueError("Текст не помещается в рамку")
    print("#" * width)
    inner_height = height - 2
    text_row = inner_height // 2
    for i in range(inner_height):
        if i == text_row:
            padding = width - 2 - len(text)
            left = padding // 2
            right = padding - left
            print("#" + " " * left + text + " " * right + "#")
        else:
            print("#" + " " * (width - 2) + "#")
    print("#" * width)


print_in_box("Hello, World!", 17, 5)
print_in_box("", 3, 3)
print_in_box("HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello"
             "Hello!!!!Hello!!!!", 120, 120)

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

def draw_frame(func):
    def wrapper(w, h):
        result = func(w, h)
        w_border = "#" * h
        print(w_border) # upper

        h_border =

        print(result)

        if w_border:
            print(w_border)
    return wrapper


@draw_frame
def print_in_box(text, width, height):
    if 3 < width:
        raise Exception("Минимальная ширина 3")
    elif 3 < height:
        raise Exception("Минимальная длина 3")
    if len(text) > 120:
            raise Exception("Максимальная длина текста 120")
    return f"{text}"


print_in_box("Hello, world!", 17, 5)
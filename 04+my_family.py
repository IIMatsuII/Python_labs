#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["отца", "матери", "сестры", "брата", "дедушки", "бабушки"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 165],
    [my_family[1], 156],
    [my_family[2], 154],
    [my_family[3], 145],
    [my_family[4], 152],
    [my_family[5], 160],

]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
for i in range(len(my_family)):
    print(f"Рост {my_family[i]} {my_family_height[i][1]} см")

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
my_family = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1] + my_family_height[5][1]

print(f"Общий рост моей семьи - {my_family} см")
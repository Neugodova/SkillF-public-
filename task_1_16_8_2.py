from task_16_8_2 import Rectangle, Square, Circle

# создание 2-х прямоугольников
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(5, 6)

# вывод площади 2-х прямоугольников
print(rect_1.get_area(),
      rect_2.get_area())

sq_1 = Square(5)
sq_2 = Square(10)

# вывод возведения в степень **2()

print(sq_1.get_area_square(),
      sq_2.get_area_square())

circ_1 = Circle(3)
circ_2 = Circle(5)

print(circ_1.get_area_circle(),
      circ_2.get_area_circle())

#
figures = [rect_1, rect_2, sq_1, sq_2, circ_1, circ_2]

# цикл, в котором программа выводит название фигуры
for figure in figures:
      if isinstance(figure, Square):
            print("It's a square:", figure.get_area_square())
      elif isinstance(figure, Circle):
            print("It's a circle:", figure.get_area_circle())
      else:
            print("It's a rectangle:",figure.get_area())

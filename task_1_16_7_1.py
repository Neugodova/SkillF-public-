from task_16_7_1 import Cat

cats = [
{
     "name": "Сэм",
     "gender": "мальчик",
     "age": 2,
    },
    {
     "name": "Мурка",
     "gender": "девочка",
     "age": 1,
    },
{
     "name": "Пушок",
     "gender": "мальчик",
     "age": 3,
    },
]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_dict(cat)
    print(f"Имя котика: {cat_obj.name}",f"Пол: {cat_obj.gender}", f"Возраст: {cat_obj.age}")


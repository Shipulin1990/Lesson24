class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        house_name = args[0] if args else "No name"
        obj = super().__new__()
        cls.houses_history.append(house_name)
        return obj

    def __init__(self, house_name, number_of_floors):
        self.house_name = house_name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.house_name} снесён, но остается в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 10)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)

class Builder:
    def __init__(self):
        self.obj = {}

    def update_inner_value(self, keys, value):
        if not isinstance(keys, list):  # если переданный ключ один, то присваиваем ему значение
            self.obj[keys] = value
        else:
            temp = self.obj  # в temp сохраняем объект, сгенерированный в фикстуре
            for item in keys[:-1]:  # итерируемся по списку переданных ключей, не затрагивая последний
                if item not in temp.keys():  # если переданного ключа нет в исходном объекте
                    temp[item] = {}  # создаем ключ с пустым объектом
                temp = temp[item]  # спускаемся на уровень ниже с ключом item
            temp[keys[-1]] = value  # присваиваем последнему переданному ключу значение
        return self

    def build(self):
        return self.obj

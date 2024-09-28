class House:
    def __init__ ( self ,name,number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors
    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
    def __len__(self):
        print(f'{self.number_of_floors}')
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def  __lt__(self , other ):
        return self.number_of_floors < other.number_of_floors
    def __le__(self , other ):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        self.number_of_floors += value
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return self
    def __radd__(self, value):
        self.number_of_floors += value
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return self
    def __iadd__(self, value):
        self.number_of_floors += value
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return self
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h1.__str__()
h2.__str__()
print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
h1.__add__( 10 )
print(h1 == h2)
h1.__radd__( 10 )
h1.__radd__( 20 )
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__




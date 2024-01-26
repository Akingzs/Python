class Car:
    def __init__(self):
        self._brand = None
        self._model = None
        self._year = None
        
    def show_detail(self):
        return f'Marca: {self._brand}\nModelo: {self._model}\nAno: {self._year}'

    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand
        
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, model):
        self._model = model
        
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, year):
        self._year = year

class Dono:    
    def __init__(self, nome, idade):
        self._name = nome
        self._age = idade
        # List inside init to create a new list in each instance // list before init you can modify everywhere
        # and that change will change the other instances too
        self._cars_list = []
        
    def buy_car(self,marca, modelo, ano):
        # Composition using the Car classe
        # How I used setters I need to create a new instance to set all features and then append to list
        carro = Car()
        carro.brand = marca
        carro.model = modelo
        carro.year = ano
        self._cars_list.append(carro)
    
    def sell_cars(self, car_model):
        for car in self._cars_list:
            if str(car._model).lower() == car_model:
                self._cars_list.remove(car)
                print(f'{car_model} sold')
    
    def show_cars(self):
        for car in self._cars_list:
            # Calling the car attributes needs to be by calling the instance obj "." attr
            # cause in the list we have instances of an obj 
            print(f'{self._name} has a/an {car._model} {car._year}')
    
    
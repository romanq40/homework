class Car:
    def __init__(self,colour,liters):
        self.colour = colour
        self.liters = liters
        self.fuel_consumption = 0.1
        self.mileage = 0

    def drive(self):
        km = int(input('Сколько км вы хотите проехать'))
        liter = km*0.1
        if self.liters > liter:
            self.liters -= liter
            self.mileage += km
            print(f'Мы проехали {km}км на {self.colour} машине')
        else:
            print('Не хватает топлива')

    def get_mileage(self):
        return self.mileage
    
car1 = Car(colour= 'красный',liters= 20)
print(car1.drive())
print(car1.get_mileage())
class Car:
    __yearModel = 0
    __make = "car"
    __speed = 0
    def __init__(self,yearModel,make,speedCar):
        self.set__model(yearModel)
        self.set__carManufacturer(make)
        self.set__speed(speedCar)
        self.set__acceleration(speedCar)
        self.set__brake(speedCar)
        
    def set__model(self, yearModel):
        self.__model = yearModel

    def get__model(self):
        return self.__model

    def set__carManufacturer(self, make):
        self.__carManufacturer = make

    def get__carManufacturer(self):
        return self.__carManufacturer
    
    def set__speed(self, speedCar):
        self.__speed = speedCar
        
    def get__speed(self):
        return self.__speed
    
    def set__acceleration(self, speedCar):
        self.__speed = speedCar + self.__speed
        
    def get__acceleration(self):
        return self.__speed
        
    def set__brake(self, speedCar):
        self.__speed = self.__speed - speedCar
        
    def get__brake(self):
        return self.__speed
        
def main():
    exampleCar = Car(2008, "ford", 5)
    exampleCar.set__model(2008)
    exampleCar.set__carManufacturer("Ford")
    exampleCar.set__speed(0)
    exampleCar.set__acceleration(5)
    exampleCar.set__brake(5)
    
    print("year is", exampleCar.get__model())
    print("make of car is", exampleCar.get__carManufacturer())
    print("speed of car is", exampleCar.get__speed())
    print("now to accelerate")

    for index in range(0,5):
        exampleCar.set__acceleration(5)
        print(exampleCar.get__speed())

    print("now to break")
              
    for index in range(0,5):
        exampleCar.set__brake(5)
        print(exampleCar.get__speed())
    
main()
    

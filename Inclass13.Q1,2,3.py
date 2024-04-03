class Vehicle:
    def __init__(self, max_speed, mileage, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        pass
    def m1(self):
        print(f'iam a generic m1() from the base Class Vehicle ')
    def __str__(self):
        return f' from the Vehicle __str___ {self.max_speed}, {self.mileage}, {self.capacity}'


#Exercise2: #create a car class

class Car (Vehicle):
    def m1(self):
        print(f'I am a car with max-speed= {self.max_speed}, mileage of {self.mileage}, with {self.capacity}')
        print(f'car fare is {self.fare()}')

    def fare(self):
        return  self.capacity*0.95
# EX3
class Bus(Vehicle):
    def m1(self):
        print(f'I am a bus with max-speed= {self.max_speed}, mileage of {self.mileage}, with{self.capacity}')
        print(f' bus fare is {self.fare()}')

    def fare(self):
        return self.capacity * 0.15

c1 = Car(240, 20, 4)
c1.m1()
print(c1)
print('_'*20)

b1 = Bus(35, 8, 50)
b1.m1()
print(b1)




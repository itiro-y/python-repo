# Ctrl + / to comment out code

# display __something__ (magic methods, dunder)
# print(dir(5))

# string_ex = 'hi'
# print(dir(string_ex))

# #methods are functions that are part of class or object functions
# print(string_ex.__len__())


# #OBJECTS
# #An object is a colection of data(variables) and methods that operate on data

#   SELF in a class as parameter always! It indicates that a certain var is from within the class
# and it must be used to refer to any var/function within class

class Car:

    #Constructor (__init__)
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print('Car started')
    
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('the car is in motion')
        else:   
            print('Start the car first')

    def stop(self):
        self.speed = 0
        print('STOP')

#Create an instance of car as a datatype/class Car()
car = Car()
car_1 = Car()

#Invoke functions of car
car.increase_speed(10)
car.start()
car.increase_speed(10)
car.stop()

#Every object has its own ID
print(id(car))
print(id(car_1))








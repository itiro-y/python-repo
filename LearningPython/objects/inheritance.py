class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    
    def start(self):
        self.started = True
        print('The vehicle has been started')

    def stop(self):
        self.speed = 0
        print('The Vehicle has stopped')
    
    def increase_speed(self, delta):
        if(self.started):
            self.speed = self.speed + delta
            print(f'the new speed is {self.speed}')
        else:
            print('You must start the Vehicle first')
 

#Car class inherits all methods and variables from vehicle class
#so, it also has: started, speed, start(), stop(), increase_spee()
class Car(Vehicle):
    trunk_open = False
    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False


class Motorcycle(Vehicle):
    #Override so Motorcycle does not inherid the partant's class constructor
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out

        #We are calling the parent's constructor manually
        super().__init__()

    #Overriding methods
    def start(self):
        self.started = True
        print('You motorcycle is started')

car = Car()
motorcycle = Motorcycle()

car.increase_speed(5)
car.start()
car.open_trunk()
car.increase_speed(10)

motorcycle.increase_speed(10)
motorcycle.start()
motorcycle.increase_speed(10)





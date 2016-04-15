# road is a graph of road-length (x axis) to time (y xis) to produce a tuple as car location (to provide it with a precise location)
# if car gets within x distance of car in front of it, it needs to slow to match speed. if one more "move" would result in a crash, the car needs to stop.
# x = car position
# y = time in seconds
# for each "turn" run through random function to determine if object will slow down (1 in 10 will)
import random

class Road:
    def __init__(self):
        self.length = 1000
        self.road_entrance

class Car:
    def __init__(self, position):
        self.max_speed = 33.33  # m/s
        self.current_speed = 0  #all cars start at a dead stop
        self.acceleration_rate = 2  # +2 per second
        self.position = position
        self.distance = 0

    # def move_car_position(self):
    #     self.position += 1
    #     return round(self.position, 2)

# decides if the driver slows down, speeds up, or
    def acceleration(self):
        if random.randint(1, 10) == 1:
            return 0 - self.acceleration_rate
        # elif distance_between_cars() == self.current_speed:
        #     self.acceleration_rate = 0
        #     return self.acceleration_rate
        else:
            self.acceleration_rate = 2
            return self.acceleration_rate

# update current speed
    def updates_speed(self):
        self.current_speed = self.current_speed + self.acceleration()
        return self.current_speed

#moves one car object
    def move_car(self):
        self.position = self.position + self.current_speed
        return self.position

#determines if the car will overtake the car in front of it in the next second. If so, car stops.
    def avoid_collision(self):
        if (self.position + self.current_speed) >= (cars[i + 1].position + cars[i + 1].current_speed):
            self.current_speed == 0

#resets the car's x value to 0, as it starts back at the beginning of the stretch of road.
    def restarts_loop(self):
        if self.position > (1000):
            self.position == 0
#
    def store_distance_bw_car(self, distance):
        print (self.position + self.current_speed)
        # return self.position + self.current_speed

    # def slows_when_approaching(self):
    #     #how close is car to next car?
    #     car1.speed = 33 m/s
    #     car1.acceleration = 2 m/s
    #         if distance_to_car_in_front < 28 m
    #             car_slows_down() #car1.speed changes, car1.accelaration changes
    #         #stop


    # def avoid_collision(self):
    #     # if car(x, y) will be greater than car_in_front(x, y) on the next turn, a collision has occured
    #     #     car needs to stop



class Simulation:

    def __init__(self):
        self.number_of_cars = 30

    def create_starting_position(self):
        x = 0
        position_list = []
        for _ in range(self.number_of_cars):
            position_list.append(x)
            x += round((1000/self.number_of_cars), 2)
        return position_list

    def create_cars(self, position_list):
        cars = [Car(position) for position in position_list]
        return cars

    def set_cars(self, cars):
#moves all cars in the simulation
        for car in cars:
            car.updates_speed()
            acceleration_rate = car.acceleration()
            move_car = car.move_car()
            print(move_car)
            print("acc: ", car.acceleration_rate)
        print ("________")
        return move_car

    # def total_distance_between_cars(self, cars):
    #     for car in cars:
    #         for i in range(29):
    #             move_car = car.store_distance_bw_car(self.distance_between_cars(car, cars[i+1]))
    #     return move_car

    def distance_between_cars(self, car1, car2):
        return car2.position - car1.position - 5




def main():
    simulation = Simulation()
    starting_position = simulation.create_starting_position()
    cars = simulation.create_cars(starting_position)
    for _ in range(10):
        move_car = simulation.set_cars(cars)
        # print(move_car)
    # print(cars[0].position)


if __name__ == "__main__":
    main()

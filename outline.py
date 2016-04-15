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
    def __init__(self, position, distance):
        self.max_speed = 33.33  # m/s
        self.current_speed = 0  # m/s
        self.acceleration_rate = 2  # m/s^2
        self.position = position  # m

    def move_car(self, distance):
        self.position += self.current_speed
        """because position is list
    #     index 0 is location on road (x-axis) and speed is meters/second,
    #     each turn is one second so meters covered is increase in distance."""
        return self.position

    # def move_car_position(self):
    #     self.position += 1
    #     return round(self.position, 2)

# decides if the driver slows down or speed up
    def acceleration(self):
        if random.randint(1, 10) == 1:
            return 0 - self.acceleration_rate
        else:
            return self.acceleration_rate
# def randomly_slows(self):
    #each turn (second) randomly select 10% of car in car object list
    #rand.randint(range(30) resulting pick corresponding index in the list objects self.speed

# update current speed
    def accelerates_car(self):
        self.current_speed = self.current_speed + self.acceleration()
        return self.current_speed




    # def speed_up(self):
    #     while self.position >
    #     While distance_to_car_in_front > car1.speed
    #         car accelerates
    #     else:
    #         car matches speed


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
    #
    #
    # def restarts_loop(self):
    #     if self.position[1] > (1000) #index for self.position points to x value of x , y pairing
    #         starts loop over


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
        for index, car in cars.items():
            move_car = car.move_car(distance_between_cars(car, cars[index+1]))

        return move_car

    def distance_between_cars(self, car1, car2):
        return car2.position - car1.position - 5
    # def get_distance(self):


def main():
    simulation = Simulation()
    starting_position = simulation.create_starting_position()
    cars = simulation.create_cars(starting_position)
    simulation.set_cars(cars)
    # print(cars[0].position)


if __name__ == "__main__":
    main()


# dictionary with car number as key and value as car object

# road is a graph of road-length (x axis) to time (y xis) to produce a tuple as car location (to provide it with a precise location)
# if car gets within x distance of car in front of it, it needs to slow to match speed. if one more "move" would result in a crash, the car needs to stop.
# x = car position
# y = time in seconds
# for each "turn" run through random function to determine if object will slow down (1 in 10 will)


class Road:
    def __init__(self):
        self.length = 1000
        self.road_entrance


class Car:
    def __init__(self, position):
        self.max_speed = 33.33  # m/s
        self.current_speed = 0 #all cars start at a dead stop
        self.acceleration_rate = 2 # +2 per second
        self.position = position

    def move_car(self):
        self.position[0] = self.position[0] + self.current_speed """these are two values of a list"""
        self.position[1] = self.position[1] + 1 """so I've added the index positions to the object attributes"""
        return self.position

# decides if the driver slows down or speed up or maintains speed
    """there may be some cases where the car is speeding up. Maybe this method becomes adjust_acceleration"""
    def acceleration(self):
        if random.randint(1, 10) == 1:
            return 0 - self.acceleration_rate
        else:
            """I suggest we figure out the acceleration algorithm here. If the cars[i + 1] (car in front)
            is farther away in meters than the speed of cars[i] (this car), it will speed up."""
            return self.acceleration_rate
            """if the car in front happens to be exactly as far away in meters as the m/s speed of this car,
            it needs to match speeds."""

# update current speed
    def accelerates_car(self):
        self.current_speed += self.acceleration()
        return self.current_speed

#determines if the car will overtake the car in front of it in the next second. If so, car stops.
    def avoid_collision(self):
        if (self.position[0] + self.current_speed) >= (cars[i + 1].position[0] + cars[i + 1].current_speed):
            self.current_speed == 0
            """not sure how to denote the next car in line, so for now I'm using [i] for index and [i + 1]
            for next car in line. Changes current speed to 0 to ensure it does not collide with the car ahead.
            Index is on .positions to denote x value in x , y lists which make up position. """

#resets the car's x value to 0, as it starts back at the beginning of the stretch of road.
    def restarts_loop(self):
        if self.position[0] > (1000):
            self.position[0] == 0



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

    # def set_cars(self, cars):
    #     move_car = Car.move_cars()
    #     return move_car


#creates "road" to begin simulation
simulation = Simulation()
#creates list of all starting locations for cars
starting_position = simulation.create_starting_position()
#takes list of all starting locations, feeds in to create all cars on road at corresponding locations
cars = simulation.create_cars(starting_position)
#attempt to build the simulation loop:
for car in cars:
    acceleration(car)
    move_car(car)
"""thinking over how the loop should work, the functions "avoid_collision" and "restarts_loop"
need to be worked into the other methods, in if/else statements. Otherwise, the loop is pretty
straightforward: at the start, it determines each car's current speed and velocity, and whether
it will slow, accelerate, or maintain, and then move all the cars. Then it repeats."""

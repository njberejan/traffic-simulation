#road is a graph of road-length (x axis) to time (y xis) to produce a tuple as car location (to provide it with a precise location)
#if car gets within x distance of car in front of it, it needs to slow to match speed. if one more "move" would result in a crash, the car needs to stop.
# x = car position
# y = time in seconds
#for each "turn" run through random function to determine if object will slow down (1 in 10 will)
class Road:
    def __init__(self):
        self.length = 1000
        self.road_entrance

class Car:
    def __init__(self):
        self.max_speed = 33.33
        self.current_speed = 0
        self.acceleration_rate = 2
        self.position = (x , y)

    def move_car(self):
        self.position = self.position[0 + self.speed, y + 1] """because position is tuple
        index 0 is location on road (x-axis) and speed is meters/second,
        each turn is one second so meters covered is increase in distance."""
        return self.position

    def accelerates_car(self):
        car1.speed = 10 m/s
        car1.acceleration = 2 m/s
        while distance_to_car_in_front > car1.speed
            car accelerates
        else:
            car matches speed

    def slows_when_approaching(self):
        #how close is car to next car?
        car1.speed = 33 m/s
        car1.acceleration = 2 m/s
            if distance_to_car_in_front < 28 m
                car_slows_down() #car1.speed changes, car1.accelaration changes
            #stop

    def randomly_slows(self):
        #each turn (second) randomly select 10% of car in car object list
        #rand.randint(range(30) resulting pick corresponding index in the list objects self.speed

    def avoid_collision(self):
        # if car(x, y) will be greater than car_in_front(x, y) on the next turn, a collision has occured
        #     car needs to stop


    def restarts_loop(self):
        if self.position[1] > (1000) #index for self.position points to x value of x , y pairing
            starts loop over

    def create_starting_position(self):
        number_of_cars = 30
        x = 0
        y = 0
        position_list = []
        for _ in range(number_of_cars):
            position_list.append([x, y])
            x += 1000/number_of_cars
        return position_list

    def create_cars(self, position_list):
        cars = [Car(position) for position in position_list]



#dictionary with car number as key and value as car object

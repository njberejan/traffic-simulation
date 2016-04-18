# Traffic Simulation

## Objectives
Analyze the behavior of drivers on a new road to determine the optimal speed limits.

### Assumptions
* Drivers want to go up to 120 km/hr.
* The average car is 5 meters long.
* Drivers want at least a number of meters equal to their speed in meters/second between them and the next car.
* Drivers will accelerate 2 m/s up to their desired speed as long as they have room to do so.
* If another car is too close, drivers will match that car's speed until they have room again.
* If a driver would hit another car by continuing, they stop.
* Drivers will randomly (10% chance each second) slow by 2 m/s.
* This section of road is one lane going one way.

## Requirements
* Python3
* Jupyter Notebook
* Required libraries in requirements.txt

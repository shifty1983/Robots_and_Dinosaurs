from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        
        
    def create_fleet(self):
        self.robot1 = Robot("Voltron", 100, 70)
        self.robot2 = Robot("Optimus Prime", 85, 85)
        self.robot3 = Robot("Astro Boy", 70, 100)
        
        self.robots.append(self.robot1)
        self.robots.append(self.robot2)
        self.robots.append(self.robot3)

    def fleet_robots(self):
        for robot in self.robots:
            print(robot.name)
   
fleet = Fleet()
fleet.create_fleet()
fleet.fleet_robots()



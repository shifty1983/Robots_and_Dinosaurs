from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        
        
    def create_fleet(self):
        self.robot1 = Robot("Voltron")
        self.robot2 = Robot("Optimus Prime")
        self.robot3 = Robot("Astro Boy")
        
        self.robots.append(self.robot1)
        self.robots.append(self.robot2)
        self.robots.append(self.robot3)

    def fleet_robots(self):
        for robot in self.robots:
            print(robot.name)
   
fleet = Fleet()
fleet.create_fleet()
fleet.fleet_robots()



from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.attacking_robots =[]
        
        
    def create_fleet(self):
        self.robot1 = Robot("Voltron")
        self.robot2 = Robot("Optimus Prime")
        self.robot3 = Robot("Astro Boy")
        
        self.robots.append(self.robot1)
        self.robots.append(self.robot2)
        self.robots.append(self.robot3)

        self.attacking_robots.append(self.robot1)
        self.attacking_robots.append(self.robot2)
        self.attacking_robots.append(self.robot3)
    
    def current_fleet(self):
        print ("Defending Robot Fleet:")
        i = 0
        for robot in self.robots:
            print(f'Press {i} to select {robot.name} (health {robot.health}, power {robot.power})')
            i += 1
    
    def attacking_fleet(self):
        print ("Attacking Robot Fleet:")
        i = 0
        for robot in self.attacking_robots:
            print(f'Press {i} to select {robot.name} (health {robot.health}, energy {robot.power})')
            i += 1


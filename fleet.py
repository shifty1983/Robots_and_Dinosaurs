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
    
    def current_fleet(self):
        print ("Current Robot Fleet:")
        i = 0
        for robot in self.robots:
            print(f'Press {i} to select {robot.name} (health {robot.health}, power {robot.power})')
            i += 1

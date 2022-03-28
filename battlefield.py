from pickle import FALSE, TRUE
from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.battle()

    def display_welcome(self):
        print ('Weclome to the Battle Royale')
        print ('*****************************************************')

    def battle(self):
        battle = True
        while battle == True:
            turn = random.randint(1, 2)
            if turn == 1:
                self.robo_turn()
            elif turn == 2:
                self.dino_turn()
            
            if len(self.fleet.robots) == 0 or len(self.herd.dinosaurs) == 0:
                self.display_winner()
                battle = False

    def dino_turn(self):
        self.show_dino_attacking_options()
        
        dinosaur_choice = int(input("Select dinosaur to attack with: "))
        if dinosaur_choice == 0:
            self.attacking_dinosaur = self.herd.attacking_dinosaurs[0]
        elif dinosaur_choice == 1:
            self.attacking_dinosaur = self.herd.attacking_dinosaurs[1]
        else:
            self.attacking_dinosaur = self.herd.attacking_dinosaurs[2]

        self.show_dino_opponent_options()

        robot_choice = int(input("Select robot to attack: "))
        if robot_choice == 0:
            self.attacked_robot = self.fleet.robots[0]
        elif robot_choice == 1:
            self.attacked_robot = self.fleet.robots[1]
        else:
            self.attacked_robot = self.fleet.robots[2]

        self.attacking_dinosaur.attack(self.attacked_robot)
        
        self.attacking_dinosaur.energy -= 10

        if self.attacked_robot.health <= 0:
            self.fleet.robots.remove(self.attacked_robot)
        
        if self.attacked_robot.health <=0 and self.attacked_robot in self.fleet.attacking_robots:
            self.fleet.attacking_robots.remove(self.attacked_robot)
            
        if self.attacking_dinosaur.energy <= 0:
            self.herd.attacking_dinosaurs.remove(self.attacking_dinosaur)

    def robo_turn(self):
        self.show_robo_attacking_options()

        robot_choice = int(input("Select robot to attack with: "))
        if robot_choice == 0:
            self.attacking_robot = self.fleet.attacking_robots[0]
        elif robot_choice == 1:
            self.attacking_robot = self.fleet.attacking_robots[1]
        else:
            self.attacking_robot = self.fleet.attacking_robots[2]

        self.show_robo_opponent_options()

        dino_choice = int(input("Select dinosaur to attack: "))
        if dino_choice == 0:
            self.attacked_dino = self.herd.dinosaurs[0]
        elif dino_choice == 1:
            self.attacked_dino = self.herd.dinosaurs[1]
        else:
            self.attacked_dino = self.herd.dinosaurs[2]

        self.attacking_robot.attack(self.attacked_dino)
        
        self.attacking_robot.power -= 10

        if self.attacked_dino.health <=0 :
            self.herd.dinosaurs.remove(self.attacked_dino)  
            
        if self.attacked_dino.health <= 0 and self.attacked_dino in self.herd.attacking_dinosaurs:
            self.herd.attacking_dinosaurs.remove(self.attacked_dino)  
        
        if self.attacking_robot.power <= 0:
            self.fleet.attacking_robots.remove(self.attacking_robot)
        
    def show_dino_opponent_options(self):
        self.fleet.current_fleet()
    
    def show_dino_attacking_options(self):
        self.herd.attacking_herd()

    def show_robo_opponent_options(self):
        self.herd.current_herd()
    
    def show_robo_attacking_options(self):
        self.fleet.attacking_fleet()
        

    def display_winner(self):
        if len(self.fleet.robots) == 0:
            print ("The Dinosaurs have destroyed the Robots and are victorious")
            
        elif len(self.herd.dinosaurs) == 0:
            print ("The Dinosaurs have destroyed the Robots and are victorious")

battlefield = Battlefield()
battlefield.run_game()  
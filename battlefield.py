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
            else:
                self.dino_turn()
            
            self.display_winner()

    def dino_turn(self):
        self.herd.current_herd()
        
        dinosaur_choice = int(input("Select dinosaur to attack with: "))
        if dinosaur_choice == 0:
            self.attacking_dinosaur = self.herd.dinosaurs[0]
        elif dinosaur_choice == 1:
            self.attacking_dinosaur = self.herd.dinosaurs[1]
        else:
            self.attacking_dinosaur = self.herd.dinosaurs[2]

        self.show_robo_opponent_options()

        robot_choice = int(input("Select robot to attack: "))
        if robot_choice == 0:
            self.attacked_robot = self.fleet.robots[0]
        elif robot_choice == 1:
            self.attacked_robot = self.fleet.robots[1]
        else:
            self.attacked_robot = self.fleet.robots[2]

        self.attacking_dinosaur.attack(self.attacked_robot)
        
        self.attacking_dinosaur.energy -= 10

        if self.attacked_robot.health <=0:
            self.fleet.robots.remove(self.attacked_robot)

    def robo_turn(self):
        self.fleet.current_fleet()

        robot_choice = int(input("Select robot to attack with: "))
        if robot_choice == 0:
            self.attacking_robot = self.fleet.robots[0]
        elif robot_choice == 1:
            self.attacking_robot = self.fleet.robots[1]
        else:
            self.attacking_robot = self.fleet.robots[2]

        self.show_dino_opponent_options()

        dino_choice = int(input("Select dinosaur to attack: "))
        if dino_choice == 0:
            self.attacked_dino = self.herd.dinosaurs[0]
        elif dino_choice == 1:
            self.attacked_dino = self.herd.dinosaurs[1]
        else:
            self.attacked_dino = self.herd.dinosaurs[20]

        self.attacking_robot.attack(self.attacked_dino)
        
        self.attacking_robot.power -= 10

        if self.attacked_dino.health <=0:
            self.herd.dinosaurs.remove(self.attacked_dino)
        
    def show_dino_opponent_options(self):
        self.fleet.current_fleet()

    def show_robo_opponent_options(self):
        self.herd.current_herd()
        

    def display_winner(self):
        if len(self.fleet.robots) == 0:
            print ("The Dinosaurs have destroyed the Robots and are victorious")
            battle = False
        elif len(self.herd.dinosaurs) == 0:
            print ("The Dinosaurs have destroyed the Robots and are victorious")
            battle = False

battlefield = Battlefield()
battlefield.run_game()  
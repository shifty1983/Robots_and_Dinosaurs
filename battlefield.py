from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.battle()
    def display_welcome(self):
        print ('Weclome to the Battle Royale')
        print ('*****************************************************')

    def battle(self):
        # turn = random.randint(1, 2)
        turn = 1
        if turn == 1:
            self.fleet.current_fleet()

            self.robot_choice = int(input("Select robot to attack with: "))
            if self.robot_choice == 0:
                self.attacking_robot = self.fleet.robot1
            elif self.robot_choice == 1:
                self.attacking_robot = self.fleet.robot2
            else:
                self.attacking_robot = self.fleet.robot3
            
            self.robo_turn(self.attacking_robot)

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        self.herd.current_herd()

        dino_choice = int(input("Select dinosaur to attack: "))
        if dino_choice == 0:
            self.attacked_dino = self.herd.dinosaur1
        elif dino_choice == 1:
            self.attacked_dino = self.herd.dinosaur2
        else:
            self.attacked_dino = self.herd.dinosaur3

        self.attacking_robot.attack(self.attacked_dino)
        
        self.attacking_robot.power -= 10
        
    def show_dino_opponent_option(self):
        self.fleet.current_fleet()

    def show_robo_opponent_options(self):
        self.herd.current_herd()
        

    def display_winner(self):
        pass

battlefield = Battlefield()
battlefield.run_game()  
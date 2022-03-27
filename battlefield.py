from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.show_dino_opponent_option()
        self.show_robo_opponent_options()
    def display_welcome(self):
        print ('Weclome to the Battle Royale')
        print ('*****************************************************')

    def battle(self):
        pass
     
    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_option(self):
        self.fleet.current_fleet()

    def show_robo_opponent_options(self):
        self.herd.current_herd()

    def display_winner(self):
        pass

battlefield = Battlefield()
battlefield.run_game()  
from PyInquirer import prompt
from weapon import Weapon

class Robot:
    weapon1 = Weapon('Photon Canon', 40)
    weapon2 = Weapon('Laser', 30)
    weapon3 = Weapon('Rocket', 20)
    weapon_list = [weapon1, weapon2, weapon3]
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 50
        
    def attack(self, dinosaur):
        print ('What weapon do you choose to attack with?')
        
        i = 0
        for weapon in Robot.weapon_list:
            print(f'Press {i} to use {weapon.name} (attack power {weapon.attack_power})')
            i += 1
            
        weapon_selection = int(input('Select weapon to use: '))
        if weapon_selection == 0:
            self.weapon = Robot.weapon1
        elif weapon_selection == 1:
            self.weapon = Robot.weapon2
        else:
            self.weapon = Robot.weapon3

        dinosaur.health -= self.weapon.attack_power
        print (f'{dinosaur.name} was hit with a {self.weapon.name} for {self.weapon.attack_power} damage!')
        if dinosaur.health <= 0:
            print (f'{dinosaur.name} has been killed!')
        print ('*****************************************************')
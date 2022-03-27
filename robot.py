from PyInquirer import prompt
from weapon import Weapon

class Robot:
    weapon1 = Weapon('Photon Canon', 50, 60)
    weapon2 = Weapon('Laser', 35, 45)
    weapon3 = Weapon('Rocket', 20, 30)
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
    def attack(self, dinosaur):
        pass

    def choose_weapon(self, name):
        answers = prompt([
            {
                'type': 'list',
                'name': 'weapon',
                'message': (f'What weapon do you choose to attack with?'),
                'choices': [(f'{Robot.weapon1.name} (attack power {Robot.weapon1.attack_power}, power depletion {Robot.weapon1.power_depletion})'), 
                            (f'{Robot.weapon2.name} (attack power {Robot.weapon2.attack_power}, power depletion {Robot.weapon2.power_depletion})'),
                            (f'{Robot.weapon3.name} (attack power {Robot.weapon3.attack_power}, power depletion {Robot.weapon3.power_depletion})')],
            }
        ])
        
        self.weapon = answers['weapon']
        return(self.weapon)

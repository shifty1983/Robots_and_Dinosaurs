class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.energy = 50
        
    def attack(self, robot):
        attack_tuple =('Bite', 'Stomp','Slash')
        print ('How do you want to attack?')
        
        i = 0
        for attack in attack_tuple:
            print(f'Press {i} to use {attack}')
            i += 1
        
        attack_selection = int(input('Select attack to use: '))
        if attack_selection == 0:
            attack = 'Bite'
        elif attack_selection == 1:
            attack = 'Stomp'
        else:
            attack = 'Slash'

        robot.health -= self.attack_power
        print (f'{robot.name} was hit with {attack} for {self.attack_power} damage!')
        if robot.health <= 0:
            print (f'{robot.name} has been destroyed!')
        print ('*****************************************************')
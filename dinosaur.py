from attack_type import AttackType

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_type = AttackType()
        self.energy = 30

    def attack(self, robot):
        pass
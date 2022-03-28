from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []  
        
    def create_herd(self):
        self.dinosaur1 = Dinosaur("Godzilla",40)
        self.dinosaur2 = Dinosaur("Blue", 35)
        self.dinosaur3 = Dinosaur("Rex", 30)
        
        self.dinosaurs.append(self.dinosaur1)
        self.dinosaurs.append(self.dinosaur2)
        self.dinosaurs.append(self.dinosaur3)

    def current_herd(self):
        print ("Current Dinosaur Herd:")
        i = 0
        for dinosaur in self.dinosaurs:
            print(f'Press {i} to select {dinosaur.name} (health {dinosaur.health}, energy {dinosaur.energy})')
            i += 1
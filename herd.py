from dinosaur import Dinosaur

class Fleet:
    def __init__(self):
        self.dinosaurs = []  
        
    def create_fleet(self):
        self.dinosaur1 = Dinosaur("Godzilla",70)
        self.dinosaur2 = Dinosaur("Blue", 85)
        self.dinosaur3 = Dinosaur("Rex", 70)
        
        self.dinosaurs.append(self.dinosaur1)
        self.dinosaurs.append(self.dinosaur2)
        self.dinosaurs.append(self.dinosaur3)

    def herd_dinosaurs(self):
        for dinosaur in self.dinosaurs:
            print(dinosaur.name)
   
herd = Fleet()
herd.create_fleet()
herd.herd_dinosaurs()
class mobs:
    def __init__(self, health, attack, drops):
        self.health = health
        self.attack = attack
        self.drops = drops
        
class Ogre(mobs):
    def __init__(self, name, health, attack, drops):
        self.name = name
        super().__init__(health, attack, drops)

x = Ogre("Ogre", 100, 10, 10)
for key, item in x.__dict__.items():
    print(f"{key} : {item}")

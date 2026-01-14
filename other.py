class mobs:
    def __init__(self, health, attack, drops):
        self.health = health
        self.attack = attack
        self.drops = drops
class Ogre(mobs):
    def __init__(self, health, attack, drops):
        super().__init__(health, attack, drops)

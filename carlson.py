Shop = [ 
{ "weapon" : "Iron Sword", "attack" : 35},
{ "weapon" : "Ice Sword", "attack" : 50},
{ "weapon" : "Fire Sword", "attack" : 60}
]

class player:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self. inventory = inventory
    def earn(self, value):
        self.money += value
    def show_balance(self):
        print(f"You have {self.money}")
    def buy(self, item):
        self.inventory.append(item)

name = input("Name your hero")
name = player(f"{name}", 100, [{"weapon": "wooden sword", "attack" : 15}])
for key, value in name.__dict__.items():
    print(f"{key}: {value}")





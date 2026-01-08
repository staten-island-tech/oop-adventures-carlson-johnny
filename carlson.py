Shop = [ 
{ "weapon" : "Iron Sword", "attack" : 35, "price" : 50},
{ "weapon" : "Ice Sword", "attack" : 50, "price": 75},
{ "weapon" : "Fire Sword", "attack" : 60, "price": 95}
]

class player:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def earn(self, value):
        self.money += value
    def show_balance(self):
        print(f"You have {self.money}")
    def buy(self, item):
        self.inventory.append(item)
    def spend(self, value):
        name.money -= value
    '''def multipliers(self, value):'''
        

name = input("Name your hero")
name = player(f"{name}", 100, [{"weapon": "wooden sword", "attack" : 15}])
for key, value in name.__dict__.items():
    print(f"{key}: {value}")



shopping = input("buy something")
for item in Shop:
    if shopping in item["weapon"]:
        name.buy(item)
        name.spend(item["price"])
        for key, value in name.__dict__.items():
            print(f"{key}: {value}")





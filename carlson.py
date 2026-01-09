Shop = [ 
{ "weapon" : "Iron Sword", "attack" : 35, "price" : 50},
{ "weapon" : "Ice Sword", "attack" : 50, "price": 75},
{ "weapon" : "Fire Sword", "attack" : 60, "price": 95}
]

class player:
    def __init__(self, name, money, inventory, money_buff):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.money_buff = money_buff
    def earn(self, value):
        self.money += value * self.money_buff
    def show_balance(self):
        print(f"You have {self.money}")
    def buy(self, item):
        self.inventory.append(item)
    def spend(self, value):
        name.money -= value
    '''def multipliers(self, value):'''
        

name = input("Name your hero")
name = player(f"{name}", 100, [{"weapon": "wooden sword", "attack" : 15}], 1.0)
name.money_buff(1.2)
name.earn(10)
for key, value in name.__dict__.items():
    print(f"{key}: {value}")

'''Do = input("Choose something to do. 1.Adventure.")
if Do == "Adventure":'''


'''shopping = input("buy something")
for item in Shop:
    if shopping in item["weapon"]:
        name.buy(item)
        name.spend(item["price"])
        for key, value in name.__dict__.items():
            print(f"{key}: {value}")'''






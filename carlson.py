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
    
        

name = input("Name your hero")
name = player(f"{name}", 100, [{"weapon": "wooden sword", "attack" : 15}], 1.0)


Do = input("Choose something to do. 1.Adventure.  2.Shop")
if Do == "Adventure":
    print("Starting Adventure")
    

if Do == "Shop":
    shopping = input("buy something")
    found = False
    for item in Shop:
        if shopping in item["weapon"]:
            name.buy(item)
            name.spend(item["price"])
            found = True
            break
        if shopping not in item["weapon"]:
            print("item not found")
        for key, value in name.__dict__.items():
            print(f"{key}: {value}")






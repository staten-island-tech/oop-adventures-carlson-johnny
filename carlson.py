class player:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self. inventory = inventory
    def earn(self, value):
        self.money += value
    def show_balance(self):
        print(f"You have {self.money}")

name = input("Name your hero")
name = player(f"{name}", 100, ["wooden sword"])
name.inventory.append("Ice Sword")
for key, value in name.__dict__.items():
    print(f"{key}: {value}")



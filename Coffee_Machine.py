class Coffee_Machine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    

def main():
    mr_coffee = Coffee_Machine()
    coffee_inventory(mr_coffee)
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    while action != "exit":
        action = input()
        if action == "buy":
            print()
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            try:
                item = int(input())
            except: 
                print()
                item = 0
            if item == 1:
                if enough_inventory(mr_coffee, item):
                    serve_coffee(mr_coffee, item)
            elif item == 2:
                if enough_inventory(mr_coffee, item):
                    serve_coffee(mr_coffee, item)
            elif item == 3:
                if enough_inventory(mr_coffee, 3):
                    serve_coffee(mr_coffee, 3)
            else:
                print("Invalid option")
        elif action == "fill":
            fill_machine(mr_coffee)
        elif action == "take":
            take(mr_coffee)
        elif action == "remaining":
            coffee_inventory(mr_coffee)
        elif action == "exit":
            break
        else:
            "Invalid output"
    print()

def buy_coffee():
    print()
    print("Write action (buy, fill, take):")
  
def coffee_inventory(machine):
    print("The coffee machine has:")
    print(machine.water, "of water")
    print(machine.milk, "of milk")
    print(machine.beans, "of beans")
    print(machine.cups, "of cups")
    print(machine.money, "of money")
    print()
    
    
def serve_coffee(coffee, item):
    if item == 1:
        coffee.water = coffee.water - 250
        coffee.beans = coffee.beans - 16
        coffee.money = coffee.money + 4
        coffee.cups = coffee.cups - 1
    elif item == 2:
        coffee.water = coffee.water - 350
        coffee.milk = coffee.milk - 75
        coffee.beans = coffee.beans - 20
        coffee.money = coffee.money + 7
        coffee.cups = coffee.cups - 1
    elif item == 3:
        coffee.water = coffee.water - 200
        coffee.milk = coffee.milk - 100
        coffee.beans = coffee.beans - 12
        coffee.money = coffee.money + 6
        coffee.cups = coffee.cups - 1
        
def enough_inventory(coffee, item):
    enough_cups = coffee.cups >= 1
    if item == 1:
        if enough_cups is False:
            print("Sorry, not enough cups")
            return False
        elif coffee.water >= 250 and coffee.beans >= 16 and enough_cups:
            print("I have enough resources, making you a coffee!")
            return True
        else:
            if coffee.water < 250:
                print("Sorry, not enough water")
            elif coffee.beans < 16:
                print("Sorry, not enough beans")
            return False
    elif item == 2:
        if enough_cups is False:
            print("Sorry, not enough cups")
            return False
        elif coffee.water >= 350 and coffee.beans >= 20 and coffee.milk >=  75 and enough_cups:
            print("I have enough resources, making you a coffee!")
            return True
        else:
            if coffee.water < 350:
                print("Sorry, not enough water")
               
            elif coffee.beans < 20:
                print("Sorry, not enough coffee")
                
            elif coffee.milk < 75:
                print("Sorry, not enough milk")
                
            return False
    elif item == 3:
        if enough_cups is False:
            print("Sorry, not enough cups")
            return False
        elif coffee.water >= 200 and coffee.beans >= 100 and coffee.milk >=  12 and enough_cups:
            print("I have enough resources, making you a coffee!")
            return True
        else:
            if coffee.water < 200:
                print("Sorry, not enough water")
            elif coffee.beans < 100:
                print("Sorry, not enough coffee")
            elif coffee.milk < 12:
                print("Sorry, not enough milk")
            return False
    print()

def fill_machine(machine):
    
    print("Write how many ml of water do you want to add:")
    water_fill = int(input())
    machine.water = machine.water + water_fill
    print("Write how many ml of milk do you want to add:")
    milk_fill = int(input())
    machine.milk = machine.milk + milk_fill
    print("Write how many grams of coffee beans do you want to add:")
    bean_fill = int(input())
    machine.beans = machine.beans + bean_fill
    print("Write how many disposable cups of coffee do you want to add:")
    cup_fill = int(input())
    machine.cups = machine.cups + cup_fill
    print()
    
def take(machine):
    print("I gave you $", machine.money)
    machine.money = machine.money - machine.money
    print()

if __name__ == "__main__":
    
    main()


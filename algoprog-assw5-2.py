class Lex: 
    def __init__(self):
        self.health = 100
        self.inventory = []
        self.money = 1000
    
    def fightenemies (self) : 
        if self.health == 0 :
            print(f"Bruh, You are DEAD.")
            exit()
        else :
            self.health -= 20
            self.money += 10
            print (f"You've defeated the enemies. Health : {self.health}, Your money has been increased : {self.money}")
    def heal (self) : 
        if self.health == 100 : 
            print(f"Your health is already full. Health : {self.health}")
        else : 
            self.health += 20
            print(f"You've been healed. Health : {self.health}")
    
    def buystuffs (self) : 
        items = input("Enter an item name that you want to buy : ")
        amount = int(input("How much do you want? : "))
        if self.money <= 0 :
            print("Bro... you spent too much, now there's no money left...")
        else :
            self.money -= 20*amount
            self.inventory.append(items)
            print(f"{items} have been added to you inventory. Money Left : {self.money}")

    def checkstats (self) : 
        print(f"Health : {self.health}")
        print(f"Money : {self.money}")
        print(f"Items : {self.inventory}")
        
def start ():
    lex = Lex()
    while True:
        print(f"[1] Fight some enemies!")
        print(f"[2] Buy some stuffs.")
        print(f"[3] Heal...")
        print(f"[4] Check your stats.")

        choice = input("What do you want to do? : ")

        if choice == "1":
            lex.fightenemies()
        elif choice == "2":
            lex.buystuffs()
        elif choice == "3":
            lex.heal()
        elif choice =="4":
            lex.checkstats()
        else : 
            print("Wait what?! That's not on the list!")

if __name__ == '__main__':
    start()
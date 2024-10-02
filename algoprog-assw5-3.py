class Harris: 
    def __init__(self):
        self.health = 100
        self.inventory = []
        self.money = 1000
        self.energy = 250
    
    def fightenemies (self) : 
        if self.health <= 20 :
            print(f"Your health is low, you can't fight that enemy. Health : {self.health}")
        elif self.health == 0 :
            print(f"Bruh, You are DEAD.")
        else :
            self.health -= 15
            self.money += 10
            self.energy -= 30
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
        if self.money == 0 :
            print("Bro... you spent too much, now there's no money left...")
        else :
            self.money -= 20*amount
            self.inventory.append(items)
            print(f"{items} have been added to you inventory. Money Left : {self.money}")
    
    def work (self) :
        if self.energy == 0 :
            print ("You've been working all day, now you are tired. Get Some Rest!")
        else :
            self.energy -= 20
            self.money += 30
            print(f"Hooray! Your money has been increased : {self.money} ")
    
    def rest (self) : 
        if self.energy == 250 : 
            print("You already have a long rest, GO BACK TO WORK!")
        else : 
            self.energy += 50
            print(f"HOAMMMMM.... What a good sleep.... Your energy now is : {self.energy}")

    def checkstats (self) : 
        print(f"Health : {self.health}")
        print(f"Money : {self.money}")
        print(f"Items : {self.inventory}")
        
def start ():
    haha = Harris()
    while True:
        print(f"[1] Fight some enemies!")
        print(f"[2] Buy some stuffs.")
        print(f"[3] WORK! WORK! WORK!")
        print(f"[4] Rest...")
        print(f"[5] Heal...")
        print(f"[6] Check your stats.")

        choice = input("What do you want to do? : ")

        if choice == "1":
            haha.fightenemies()
        elif choice == "2":
            haha.buystuffs()
        elif choice == "3":
            haha.work()
        elif choice == "4":
            haha.rest()
        elif choice == "5":
            haha.heal()
        elif choice =="6":
            haha.checkstats()
        else : 
            print("Wait what?! That's not on the list!")

if __name__ == '__main__':
    start()
from time import sleep as wait

class Character:
    def __init__(self, name, speed, jump, hp):
        self.name = name
        self.speed = speed
        self.jump = jump
        self.hp = hp
    
    def walk(self):
        print(f" {self.name} is walking")
# I know i know the stats are straight up useless, but i was focused on inheritancing. Whole code is just a dummy test
class Zombie(Character):
    
    def __init__(self, name, speed, jump, hp, rotten_level):
        super().__init__(name, speed, jump, hp)
        self.rotten_level = rotten_level

    def fucking_backflip(self):
        print("You didn't manage to do a fucking backflip. You are a zombie, what did you even expect?")
        speed = 0
        hp = 0
        
class Human(Character):

    def __init__(self, name, speed, jump, hp, punch):
        super().__init__(name, speed, jump, hp)
        self.punch = punch

    def punch_x(self):
        print("You missed (Dont say its because of lag. Its piece of code running localy on your pc)")
        wait(2)
        print("Dies miserably out of embarasment")
        hp = 0
# Maybe i will continue this code in the future if the stars align right
zombiex = Zombie("Zombie", 10, 0, 70, "High")
humanx = Human("Human", 16, 50, 100, "Weaker than nevborns")

while True:
    option = input("Choose what you want to do: 1. Backflip (as a zombie) 2. Punch as a human: ")
    if option == "1":
        zombiex.fucking_backflip()
        break
    elif option == "2":
        humanx.punch_x()
        

        

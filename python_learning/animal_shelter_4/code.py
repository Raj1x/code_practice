class Pet:
    def __init__(self, description, species, energy, max_energy):
        self.description = description
        self.species = species
        self.energy = energy
        self.max_energy = max_energy
    def play(self):
        if self.energy == self.max_energy:
            self.energy = self.energy * 0.3
            print(f"| Your pet lost 70% of its energy while playing with you.\n| {self.energy}")
        else:
            lack_of_energy = self.max_energy - self.energy
            print(f"| Your pet isnt able to play with you.\n| He needs {lack_of_energy} more energy.")

    def gamble(self):
        print(f"{self.species} shouldnt be gambling your life savings away...\n what a silly idea")
        # might be possible and worth it in the future tho. You will never know, its called gambling not for a reason 
    
    def sleep(self):
        if self.energy == self.max_energy:
            print(f"| Your {self.species} feel like resting rn")
        else:
            gain = self.max_energy - self.energy
            self.energy = self.max_energy
            print(f"| Your {self.species} rested well... And gained {gain} energy.")
        #its very similar to last code i wrote, like its got same structure but i can promise you when i was writing it i wasnt looking at the old one its just the schematic that built inside my head pr sum
pets = {
    "Carlos": Pet("| Carlos. The retired drug dealer from texas.\n Some people say that he is like lizard. No shit maybe because he is one", "Lizard", 90, 100),
    "Diego": Pet("| Diego. Blind vegetarian ex K9.\n Nobody knows why he is vegatarian, some weird ass lady on tiktok said so.\n She cant be lying right?", "Dog", 200, 500),
    "Enrique": Pet("| Enrique. No one knows what the fuck accualy it is, but looks like it is not from the Earth", "Alien (Probably)", 999, 1000)
}

print("===== Pet care =====  (Atleast it is what they say about this weird place")
choose = input(f"\n| Which animal are you willing to take care for? {pets.keys()}: ")

if choose in pets:
    chosen_pet = pets[choose]
    print(f"\n| Selected {chosen_pet.species}")
    print(f"\n| Description {chosen_pet.description}")

else:
    print("\n| I dont speak guacamole muchacho (We doesnt have that being that you are speaking about)")
    exit

while True:
    action = input("\n| What do you want your pet to do?: \n| 1. play / 2. sleep / 3. gamble (only if the pet is over 18!) / 4. exit: ")
    if action == "1":
        chosen_pet.play()
    
    elif action == "2":
        chosen_pet.sleep()
    
    elif action == "3":
        chosen_pet.gamble()
    
    elif action == "4":
        print("| Deja a tu hermano solo consigo mismo. *dies*")
        break

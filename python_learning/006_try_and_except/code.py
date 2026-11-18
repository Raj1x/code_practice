from time import sleep as wait

mag_capacity = 17

while True:
    try:
        how_many = int(input("How much ammunitiion are you carrying around?: "))
        if how_many >= mag_capacity:
            mag_number = how_many // 17
            print(f"You can deffinetly load a gun with that many ammo. You loaded {mag_number} mags")
            wait(4)
            print("You just shot a shadow you shizofrenic dumbass *said with deep love and care*")
            break
        elif how_many < mag_capacity:
            missing = 17 - how_many
            print("You are not able to load a gun (i mean you are but not fully tho)")
            wait(3)
            print(f"You need {missing} more bullets\n I need more bullets.\n did you catch the reference? Because i did")
    except:
        print("...")
        wait(2)
        print("Learn how to type first then use a gun")

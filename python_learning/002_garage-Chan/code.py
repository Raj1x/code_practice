garage = {
    "toyota": {"model": "Old ah toyota", "oil": 30, "max_oil": 100},
    "nissan": {"model": "Nissan with 3 left wheels", "oil": 10, "max_oil": 80}
}

car_keys = ", ".join(garage.keys())
which_car = input(f"Garage-Chan: Which car do you choose to work on with?: {car_keys}: ").lower()

if which_car in garage:
    car = garage[chosen_car]
    print(f"You selected: {car['model']}. Current oil: {car['oil']}/{car['max_oil']}")

    def add_oil(car):
        target_car["oil"] = target_car["max_oil"]
        print(f"Oil refilled!\n Garage-Chan: H-h-how n-nice of ~y-you ~N-nya. Current oil: {car['oil']}")
        
    def empty_oil(car):
        target_car["oil"] = 0
        print("Oil drained.\n Garage-Chan: D-dont d-do t-that ~t-to me or ill b-b-blush *blushes*")

    while True:
        choice = int(input("\n| Choose action (type number): 1.Add_oil / 2.Empty_oil / 3.Exit: "))
        if choice == "1":
            add_oil(car)
        if choice == "2":
            empty_oil(car)
        if choice == "3":
            print("Garage-chan: ~N-no y-you c-cant l-leave t-the ~g-garage y-yet *~hmph~")
            print("*You simply dont care and walk away*")
            break
        else:
            print("Garage-Chan: You typin chinesse? Because i dont b-baka *gets annoyed*")
else:
    print("Garage-Chan: U dont have that car.\n U aint rich or sum ~m-miaw")

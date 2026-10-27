def check_personal_best(current_run, current_pb):
    try:
        if current_run > current_pb:
            math = current_run - current_pb
            return "You didnt beat your pb\n(better luck next time(did you catch the reference?(yk the song on spotyfy. Its peak isnt it?))).\nTime needed to match pb: {math}"
        elif current_run == current_pb:
            return "You matched your pb"
        elif current_run < current_pb:
            math = current_run - current_pb
            return "NEW PB {current_pb}, better than last pb by: {math}"
    except TypeError:
        print("There is some error (This whole try except thing there is straight up useless. I added it only to practice)")

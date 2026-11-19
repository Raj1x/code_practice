from time import sleep as wait
from rich.console import Console
import pyttsx3 # its only used for one word so its useless tbh yo u can delete if if u want to download this garbage

engine = pyttsx3.init()

console = Console()

print("===== Leter Counter =====")
while True:
    try:
        option = int(input("""
        | Choose One Option:
        | 1. Count Letters
        | 2. Fart
        | 3. Exit
        | 
        | Type here: """))
        try:
            if option == 1:
                word = input("""
                Type the word that you want to count the Letters of:
                |   |   |   |
                V   V   V   V
                """)
                with console.status("Initializing quantum letter scanner...") as status:
                    wait(1.5)
                    status.update("Analyzing vowels and consonants...")
                    wait(1.5)
                    status.update("Almost done...")
                    wait(1)

                    print(f"Your word '{word}' has:\n{len(word)} letters\n\n(more letters than your dih size probably)")
            elif option == 2:
                    
                print("""
                # Farts with pure wraith

                    
                You: Dies miserably
                """)
                wait(1)

                with console.status("Wait... d-did s-someone s-say...?", spinner="dots") as status:
                    wait(2)
                    status.update("...misery???")
                    wait(1.5)

                print("M-m-misery?")
                engine.say("M-m-misery?") # shi to delete with the lib
                engine.runAndWait() # shi to delete with the lib
                wait(1)
                print("Im so fucking scared")
                wait(1)
                text = "I Miss That Kind Of Misery The Kind Where You Are Nice To Me But Only In The Evening So I Ask Am I Just Dreaming"
                # yeah i wrote that shitty ah thing by hand (they were in misery while typing tha shi) 
                for word in text.split():
                    print(word)
                    wait(0.1)
                wait(1)
                print("\nI am so sorry. That shit was worse than being stuffed by big dih randy")
            elif option == 3:
                with console.status("Turning off...", spinner="line"):
                    wait(1.5)
                print("C-cya! ~O-onichan *Rubs her thighs against eachother*")
                break
            else:
                print("Invalid. I mean the input is invalid. ~N-not y-you ~m-meow ")
                    
        except ValueError:
            print("Invalid input. Please enter a valid word *Meows gently*")
    except ValueError:
        print("Son dont type shi like ts")

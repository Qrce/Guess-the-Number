import random

def main():
    current_level = 1
    max_level = 3
    tries = 1

    print("Willkommen zu: Guess The Number!")
    print("Ich denke mir eine Zahl zwischen 1-100 aus")

    while current_level <= max_level:
        secret_number = random.randint(1, 100)
        
        print(f"\nLevel {current_level}")
        
        while True:
            guess = int(input("Versuche sie zu erraten :): "))

            if guess == secret_number:
                print(f"Level {current_level} erfolgreich in {tries} Versuchen geschafft.")
                tries = 1
                current_level += 1
                if current_level > max_level:
                    print("Herzlichen Glückwunsch! Du hast alle Level gemeistert!")
                    return
                else:
                    print(f"Versuche es jetzt bei Level {current_level}")
                break
            elif guess < secret_number:
                print(f"Aktuelle Versuche: {tries}")
                print("Leider zu niedrig, versuche es erneut:")
            else:
                print(f"Aktuelle Versuche: {tries}")
                print("Ach wie schade, leider zu hoch:")
            tries += 1

if __name__ == "__main__":
    main()

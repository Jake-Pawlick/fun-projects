import os
import sys

os.system('cls')

# Get number of players
nillas = int(input("Welcome to Initiative! Please enter how many total turns there will be: "))
initiative_list = []

# Collect player names and initiative rolls
for i in range(nillas):
    name = input(f"Enter name of {i + 1}: ")
    roll = int(input(f"Enter the initiative of {name}: "))
    initiative_list.append((name, roll))

# Sort by initiative descending
initiative_list.sort(key=lambda x: x[1], reverse=True)

i = 0  # turn counter
while True:
    user_input = input("")

    if user_input == "":
        if len(initiative_list) == 0:
            print("No players left in initiative!")
            break

        round_number = (i // len(initiative_list)) + 1

        # Clear console only at the start of a new round
        if i % len(initiative_list) == 0:
            os.system('cls')
            print(f"-"*19, round_number, "-"*19)

        current_index = i % len(initiative_list)
        next_index = (i + 1) % len(initiative_list)

        print(f"it is now \033[1;34m{initiative_list[current_index][0].title()}'s\033[0m turn. "
              f"On deck is \033[1;34m{initiative_list[next_index][0].title()}\033[0m")

        i += 1  # advance turn

    elif user_input.lower() == "bye":
        sys.exit()

    elif user_input.split()[0].lower() == "delete":
        parts = user_input.split()
        if len(parts) < 2:
            print("Please specify a name to delete, e.g. 'delete goblin'")
            continue

        remove_name = parts[1]

        for j, player in enumerate(initiative_list):
            if player[0].lower() == remove_name.lower():
                del initiative_list[j]

                # Adjust turn counter if deleted player was before current turn
                current_index = i % len(initiative_list) if len(initiative_list) > 0 else 0
                if j < current_index:
                    i -= 1

                print(f"{remove_name.title()} has been removed from initiative.")
                break
        else:
            print(f"No player named '{remove_name}' found in initiative.")

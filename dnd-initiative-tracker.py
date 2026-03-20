import os
import sys

os.system('cls')

# Setup
nillas = int(input("Welcome to Initiative! Please enter how many total turns there will be: "))
initiative_list = []
pending_additions = []

for i in range(nillas):
    name = input(f"Enter name of {i + 1}: ")
    roll = float(input(f"Enter the initiative of {name}: "))
    initiative_list.append((name, roll))

initiative_list.sort(key=lambda x: x[1], reverse=True)

current_index = 0
round_number = 1

while True:
    user_input = input("")

    if user_input == "":
        if not initiative_list:
            print("No players left in initiative!")
            break

        # Start of round
        if current_index == 0:
            if pending_additions:
                initiative_list.extend(pending_additions)
                pending_additions.clear()
                initiative_list.sort(key=lambda x: x[1], reverse=True)

                # Keep same player after re-sort
                current_index = 0

            os.system('cls')
            print(f"{'-'*19} {round_number} {'-'*19}")

        next_index = (current_index + 1) % len(initiative_list)

        print(
            f"it is now \033[1;34m{initiative_list[current_index][0].title()}'s\033[0m turn. "
            f"On deck is \033[1;34m{initiative_list[next_index][0].title()}\033[0m"
        )

        if pending_additions:
            print(f"Joining next round: {[p[0].title() for p in pending_additions]}")

        # Advance turn
        current_index += 1

        if current_index >= len(initiative_list):
            current_index = 0
            round_number += 1

    elif user_input.lower() == "bye":
        sys.exit()

    elif user_input.startswith("delete"):
        parts = user_input.split()

        if len(parts) < 2:
            print("Usage: delete <name>")
            continue

        remove_name = parts[1].lower()

        for j, player in enumerate(initiative_list):
            if player[0].lower() == remove_name:
                del initiative_list[j]

                # Fix index shift properly
                if j < current_index:
                    current_index -= 1
                elif j == current_index:
                    # stay at same index (next person shifts into this slot)
                    pass

                if current_index >= len(initiative_list):
                    current_index = 0

                print(f"{remove_name.title()} removed.")
                break
        else:
            print("Player not found.")

    elif user_input.startswith("add"):
        parts = user_input.split()

        if len(parts) < 2:
            print("Usage: add <name>")
            continue

        add_name = parts[1]

        try:
            add_roll = float(input(f"Enter initiative for {add_name}: "))
        except ValueError:
            print("Invalid number.")
            continue

        pending_additions.append((add_name, add_roll))
        print(f"{add_name.title()} will join next round.")
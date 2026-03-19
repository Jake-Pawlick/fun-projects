import os
os.system('cls')
nillas = int(input("Welcome to Initiative! Please enter how many total turns there will be: "))
initiative_list = []

for i in range(nillas):
    name = input(f"Enter name of {i + 1}: ")
    roll = int(input(f"Enter the initiative of {name}: "))
    initiative_list.append((name, roll))

initiative_list.sort(key=lambda x: x[1], reverse=True)

i = 0
while True:
    user_input = input("")
    if user_input == "":
        round_number = (i // len(initiative_list)) + 1
        if i % len(initiative_list) == 0:   # new round started
            os.system('cls')
            print(f"-"*19,round_number,"-"*19)
        current_index = i % len(initiative_list)
        next_index = (i + 1) % len(initiative_list)
        print(f"it is now \033[1;33m{initiative_list[current_index][0]}'s\033[0m turn. On deck is \033[1;32m{initiative_list[next_index][0]}\033[0m")
        i += 1
    elif user_input.lower() == "bye":
        break
print("Welcome to the Dice Rolling Game!")
number_of_dice = int(input("How many dice do you want to roll?: "))
count_sessions = 0
while True:
    print("Roll the dice? (y/n): ")
    choice = input().strip().lower()
    if choice == 'y':
        count_sessions += 1
        import random
        dice_rolled = number_of_dice
        dice_rolled_list = []
        while dice_rolled > 0:
            dice_rolled_list.append(random.randint(1, 6))
            dice_rolled -= 1
        print(f"({dice_rolled_list})")
    else:
        print("Thanks for playing!")
        break
print(f"{count_sessions} sessions were played by the user")
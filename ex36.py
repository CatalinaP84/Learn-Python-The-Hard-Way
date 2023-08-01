from sys import exit


def lobby():
    print("You're exit in the second floor. In this place are three boxes. Which one do you take?")

    choice = input("> ")

    if choice == "1":
        print("Here is food. Now you have what to eat.")
    elif choice == "2":
        print("Here are money. Good job, you can buy what you want!")
    elif choice == "3":
        dead("The box is empty. You are starving.")
    else:
        print("You have to choose one.")


def hotel():
    print("You enter in the hotel.")
    print("There are two ways: on 'the stairs' or you take 'the elevator'.")
    print("Which one do you choose?")

    choice = input("> ")

    if choice == "the stairs":
        dead("You're starving. There it's working and the access door is locked.")
    elif choice == "the elevator":
        print("You can now go to two floors. What button do you press?")

        choice = input("> ")

        if choice == "1":
            dead("Here is the reception, but nobody is here. Good-bye!")
        elif choice == "2":
            lobby()
        else:
            print("You have to choose between first or second floor.")
    else:
        print("I got no idea that means.")


def bank():
    print("At the Bank you hope to access your money from your account.")
    print("Do you think you'll get money only saying your 'name' or some 'food'?")

    choice = input("> ")

    if "name" in choice:
        start()
    elif "food" in choice:
        dead("There is nothing to eat!")
    else:
        bank()


def dead(why):
    print(why, "Unfortunately, you're starving!")
    exit(0)


def start():
    print("You are on the street.")
    print("You're hungry but you have no money, no cards and no ID.")
    print("There is a hotel in your 'left' and a bank in your 'right'.")
    print("In which one do you enter?")

    choice = input("> ")

    if choice == "left":
        hotel()
    elif choice == "right":
        bank()
    else:
        dead("You are very hungry!")


start()

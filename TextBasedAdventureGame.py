room_list = []
# Dungeon 0
room = ["You are in a dark dungeon with 2 doors, one to the north and one to the east.", 3, 1, "None", "None"]
room_list.append(room)
# Armory 1
room = ["You find yourself in an armory surrounded by weapons, there is a door to your east. However, you notice \
a secret tunnel to your north and a door to your west also", 4, 2, "None", 0]
room_list.append(room)
# Dining hall 2
room = ["You realize you are in a dining hall surrounded by food, there is a door to your north and your east", 5,
        "None", "None", 1]
room_list.append(room)
# Bedroom 3
room = ["You find yourself in a bedroom, you can go back to the dungeon south, but you also find a secret \
tunnel to the east", "None", 4, 0, "None"]
room_list.append(room)
# Secret Tunnel 4
room = ["You are in a secret tunnel, it looks like their is an opening to your north, south, east and west. Choose \
wisely . . .", 6, 5, 1, 3]
room_list.append(room)
# Kitchen 5
room = ["You find yourself in a kitchen, there is a secret tunnel to your west and another room to your south", "None",
        "None", 2, 4]
room_list.append(room)
# Beach 6
room = ["The tunnel opens to a beautiful beach, there is a boat to your north or the tunnel to your south", 7, "None",
        4, "None"]
room_list.append(room)
# Boat 7
boat = ["You made it out of the dungeon and on the boat to get off the island. You are sailing on to greater things :)"]
room_list.append(boat)


def main():
    current_room = 0
    done = False
    direction = ""
    while not done and direction.lower() != 'q':
        print()
        print(room_list[current_room][0])
        direction = input("Which direction do you go? (n, s, e, w - q to quit): ")
        if direction.lower() == 'n' or direction.lower() == "north":
            next_room = room_list[current_room][1]
            if next_room == "None":
                print("You can't go that way")
            else:
                current_room = next_room
            if current_room == 7:
                print()
                print(room_list[current_room][0])
                done = True
        elif direction.lower() == 'e' or direction.lower() == "east":
            next_room = room_list[current_room][2]
            if next_room == "None":
                print("You can't go that way")
            else:
                current_room = next_room
            if current_room == 7:
                print()
                print(room_list[current_room][0])
                done = True
        elif direction.lower() == 's' or direction.lower() == "south":
            next_room = room_list[current_room][3]
            if next_room == "None":
                print("\nYou can't go that way")
            else:
                current_room = next_room
            if current_room == 7:
                print()
                print(room_list[current_room][0])
                done = True
        elif direction.lower() == 'w' or direction.lower() == "west":
            next_room = room_list[current_room][4]
            if next_room == "None":
                print("You can't go that way")
            else:
                current_room = next_room
            if current_room == 7:
                print()
                print(room_list[current_room][0])
                done = True
        elif direction.lower() == 'q':
            print("Goodbye\n")
            break
        else:
            print("Cannot understand what you typed, please make it a direction (n, s, e, w)")


if __name__ == "__main__":
    main()

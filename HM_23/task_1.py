number_list = []


def add_to_list():
    new_number = int(input("\nEnter new number: "))
    if new_number not in number_list:
        number_list.append(new_number)
        print(f"{new_number} added to the list")
    else:
        print(f"New number {new_number} is already in the list")
    return


def delete_from_list():
    num_to_delete = int(input("\nEnter number to delete: "))
    if num_to_delete in number_list:
        number_list.remove(num_to_delete)
    else:
        print(f"There is no {num_to_delete} in the list")
    return number_list


def check_value():
    num_to_check = int(input("\nEnter number to check: "))
    if num_to_check in number_list:
        print(f"Number {num_to_check} found in the list.")
    else:
        print(f"Number {num_to_check} not found in the list")


def replace_number():
    old_num = int(input("\nEnter the number to replace: "))
    new_num = int(input("Enter a new number: "))
    replace_all = input("Replace all occurrences? (y/n): ").lower()

    if replace_all == "y":
        for i_num in range(len(number_list)):
            if number_list[i_num] == old_num:
                number_list[i_num] = new_num
    else:
        for i_num in range(len(number_list)):
            if number_list[i_num] == old_num:
                number_list[i_num] = new_num
                return

    print("Number was successfully replaced in the list")


def menu():
    print("\nMenu:")
    print("1. Add element to list")
    print("2. Remove element from list")
    print("3. Show list")
    print("4. Check if value is in list")
    print("5. Replace value in list")
    print("Q. Quit")


if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ").lower()

        match choice:
            case "1":
                add_to_list()
            case "2":
                delete_from_list()
            case "3":
                print(f"\nNumber list: {number_list}")
            case "4":
                check_value()
            case "5":
                replace_number()
            case "q":
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice")

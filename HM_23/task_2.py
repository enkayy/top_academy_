class StringStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, string):
        if len(self.stack) < self.max_size:
            self.stack.append(string)
            print(f'String "{string}" has been pushed onto the stack.')
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            popped_string = self.stack.pop()
            print(f'String "{popped_string}" has been popped from the stack.')
            return popped_string
        else:
            print("Stack is empty")
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def clear(self):
        self.stack = []
        print("Stack has been cleared.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek at an empty stack.")
            return None


def menu():
    print("\nMenu:")
    print("1. Push a string onto the stack")
    print("2. Pop a string from the stack")
    print("3. Count strings in the stack")
    print("4. Check if the stack is empty")
    print("5. Check if the stack is full")
    print("6. Clear the stack")
    print("7. Peek at the top of the stack")
    print("Q. Exit")


if __name__ == "__main__":
    size = 5
    stack = StringStack(size)

    while True:
        menu()
        choice = input("Enter your choice: ").lower()
        match choice:
            case "1":
                string_to_push = input("Enter the string to push onto the stack: ")
                stack.push(string_to_push)
            case "2":
                stack.pop()
            case "3":
                print(f"Number of strings in the stack: {stack.count()}")
            case "4":
                print(f"Is the stack empty? {stack.is_empty()}")
            case "5":
                print(f"Is the stack full? {stack.is_full()}")
            case "6":
                stack.clear()
            case "7":
                peeked_string = stack.peek()
                if peeked_string is not None:
                    print(f"Top of the stack: {peeked_string}")
            case "q":
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice.")

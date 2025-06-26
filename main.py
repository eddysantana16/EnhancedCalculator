from app.calculator_repl import CalculatorREPL

def print_welcome():
    print("\nWelcome to the Enhanced Calculator Command-Line Application!")
    print("Type commands like: add 2 3, subtract 5 1, multiply 4 6, divide 10 2")
    print("Type 'help' for full command list, 'exit' to quit.\n")

def main():
    print_welcome()
    repl = CalculatorREPL()
    while True:
        try:
            user_input = input("Enter command: ").strip()
            if not repl.process_input(user_input):
                break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()

def process_command(user_input):
    predefined_commands = ["help", "issue", "contact support"]

    user_input_lower = user_input.lower()

    for command in predefined_commands:
        if command in user_input_lower:
            if command == "help":
                print("Here is some help information.")
            elif command == "issue":

                if "login" in user_input_lower:
                    print("The issue is related to login.")
                elif "performance" in user_input_lower:
                    print("The issue is related to performance.")
                elif "error" in user_input_lower:
                    print("The issue is related to an error.")
                else:
                    print("The issue is not categorized.")
            elif command == "contact support":
                print("You can contact our support team at our number")
            return

user_problem=input("can you tell us why you are  calling?")

process_command(user_problem)

# You may uncomment the main menu and controller method below to control via command line

# If main menu and controller is commented, control mannually by calling the methods in main


import sys

class ComboLock:
    def __init__(self, secret1, secret2, secret3):
        """ Constructor of the lock, takes in 3 passcodes """
        # Checks their validity and save them as the passcode combination if valid
        self.ComboLock(secret1, secret2, secret3)
        # Inform user on how to open the lock (following right, left, right sequence is important to open the lock)
        print(f"\nInstructions: Turn right to first passcode, Turn left to second passcode, Turn right to third passcode.\n")
        # Reset the lock
        self.reset()

        # If main menu method and controller method are uncommented, then use the command line feature
        try:
            self.main_menu()
        # If commented, proceed as usual
        except AttributeError:
            ...

    def ComboLock(self, secret1, secret2, secret3):
        """ Called during itialization of the lock (works as constructor) """
        # Put the given passcodes in a list
        secrets = [secret1, secret2, secret3]

        # Loop through each passcode to ensure if they are valid
        for secret in secrets:
            # If it is not  positive integer then it invalid
            if not isinstance(secret, int) or secret <= 0:
                raise ValueError("Ticks must be a positive integer")

        # If it is positive integer then it valid and save them as the passcode combination of the lock
        self.combination = secrets


    def reset(self):
        """ Reset the entered digits and the current position """
        self.currentPosition = 0
        self.progress = {
            "secret1": {"isDone": False, "enteredDigit": None},
            "secret2": {"isDone": False, "enteredDigit": None},
            "secret3": {"isDone": False, "enteredDigit": None}
        }

        # Inform the user about the reset
        print(f"\nReset: currently on {self.currentPosition}")



    def turnLeft(self, ticks):
        """ Turn the dial to the left based on the given ticks """
        # Ensure the user give a valid ticks by checking if its a positive int
        if not isinstance(ticks, int) or ticks <= 0:
            raise ValueError("Ticks must be a positive integer")
        
        # If the the ticks is valid
        else:
            # Subtract the ticks to the current position since we are turning left
            # Also divide by 40 and get the remainder, that is necessary to wrap the values from 0 to 40
            # if current position is less than 0 (negative) it will wrap back to 39
            self.currentPosition = (self.currentPosition - ticks) % 40
            print(f"\nDone turning left: currently on {self.currentPosition}")

            # If secret1 (1st passcode) is already entered, then this is secret2 (2nd passcode)
            if self.progress["secret1"]["isDone"]:
                # Update secret2 to be done, and save the current position as a passcode for secret2
                self.progress["secret2"]["isDone"] = True
                self.progress["secret2"]["enteredDigit"] = self.currentPosition


    def turnRight(self, ticks):
        """ Turn the dial to the right based on the given ticks """
        # Ensure the user give a valid ticks by checking if its a positive int
        if not isinstance(ticks, int) or ticks <= 0:
            raise ValueError("Ticks must be a positive integer")
        
        # If the the ticks is valid
        else:
            # Add the ticks to the current position since we are turning right
            # Also divide by 40 and get the remainder, that is necessary to wrap the values from 0 to 40
            # if current position is exceeding 40 will wrap back to 0
            self.currentPosition = (self.currentPosition + ticks) % 40
            print(f"\nDone turning right: currently on {self.currentPosition}")

            # If secret2 (2nd passcode) is not yet entered, then this is secret1 (1st passcode)
            if not self.progress["secret2"]["isDone"]:
                # Update secret1 to be done, and save the current position as a passcode for secret1
                self.progress["secret1"]["isDone"] = True
                self.progress["secret1"]["enteredDigit"] = self.currentPosition

            # If secret2 (2nd passcode) is already entered, then this is secret3 (3rd passcode)
            else:
                # Update secret3 to be done, and save the current position as a passcode for secret3
                self.progress["secret3"]["isDone"] = True
                self.progress["secret3"]["enteredDigit"] = self.currentPosition

                # Since this is secret3, inform the user that they may open the lock since all passcode are entered
                print("Entered 3 numbers. Try to open it.")



    def open(self):
        """ Try to open the lock based on the entered passcode """
        # Put in a list all of the entered passcode by user
        enteredDigits = [values["enteredDigit"] for key, values in self.progress.items()]

        # If the entered passcode do not match the lock combination, inform the user about it
        if enteredDigits != self.combination:
            print("\nLock didn't open. Reset to try again.")

        # If the entered passcode matches the lock combination, inform the user about it and stop the program
        else:
            sys.exit("\nSuccessfully opened the lock!")


    # # UNCOMMENT TO CONTROL VIA COMMAND LINE

    # def main_menu(self):
    #     """ Show the user all the possible options """
    #     # Show all the options
    #     print("\n1 - Turn Left \n2 - Turn Right \n3 - Open \n4 - Reset \n5 - Exit")
    #     # Ask for a choice
    #     choice = input("\nEnter the number of what you want to do:  ")
    #     # If a choice is given redirect to controller, else ask again
    #     if choice:
    #         self.controller(choice)
    #     else:
    #         self.main_menu()

    # def controller(self, choice):
    #     """ Controls the program based on user choice in main menu """
    #     # If user input is invalid, reprompt again in the main menu
    #     if choice not in "12345":
    #         print("\nNumber choice is invalid.\n")
            
    #         # Add buffer to let user read the error message
    #         while True:
    #             if not (input("Press enter to proceed:  ")):
    #                 return self.main_menu()

    #     # If user chose 1, then ask for how many ticks to turn left
    #     if choice == "1":
    #         try:
    #             self.turnLeft(int(input("Turning Left by how many ticks:  ")))

    #         # If user input an invalid number of ticks, inform the user about it
    #         except (TypeError, ValueError):
    #             print("\nTicks must be a positive integer.\n")

    #     # If user chose 2, then ask for how many ticks to turn right
    #     elif choice == "2":
    #         try:
    #             self.turnRight(int(input("Turning Right by how many ticks:  ")))

    #         # If user input an invalid number of ticks, inform the user about it
    #         except (TypeError, ValueError):
    #             print("\nTicks must be a positive integer.\n")

    #     # If user chose 3, then try to open the lock
    #     elif choice == "3":
    #         self.open()

    #     # If user chose 4, then reset the entered passcode and bring the dial to 0
    #     elif choice == "4":
    #         self.reset()

    #     # If user chose 5, then exit the program
    #     elif choice == "5":
    #         sys.exit("\nCLosing...")

    #     # Add a buffer to let user read  message then redirect to main menu
    #     while True:
    #         if not (input("Press enter to proceed:  ")):
    #             return self.main_menu()




def main():
    # Create a lock with where its passcode is 9, 25, 2 consecutively
    a = ComboLock(9, 25, 2)

    # Turn the dial to the right by 2 ticks (first passcode)
    a.turnRight(2)
    # Turn the dial to the left by 3 ticks (second passcode)
    a.turnLeft(4)
    # Turn the dial to the right by 3 ticks (third passcode)
    a.turnRight(15)

    # Try opening the lock, (there will be a message that the entered passcode is incorrect)
    a.open()

    # Reset the entered passcode
    a.reset()

    # Turn the dial to right by 9 ticks (first passcode)
    a.turnRight(9)
    # Turn the dial to left by 24 ticks (second passcode)
    a.turnLeft(24)
    # Turn the dial to right by 17 ticks (thrid passcode)
    a.turnRight(17)

    # Try opening the lock (there will be message saying it is successful)
    a.open()



if __name__ == "__main__":
    main()
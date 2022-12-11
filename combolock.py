import sys

class ComboLock:
    def __init__(self, secret1, secret2, secret3):
        self.ComboLock(secret1, secret2, secret3)
        print(f"\nInstructions: Turn right to first number code, Turn left to second number code, Turn right to third number code.\n")
        self.reset()

        try:
            self.main_menu()
        except:
            ...

    def ComboLock(self, secret1, secret2, secret3):
        secrets = [secret1, secret2, secret3]
        
        for secret in secrets:
            if not isinstance(secret, int) or secret <= 0:
                raise ValueError("Ticks must be a positive integer")

        self.combination = secrets

    
    def __str__(self):
        return f"{self.combination}"


    def reset(self):
        self.currentPosition = 0
        self.progress = {
            "secret1": {"isDone": False, "enteredDigit": None},
            "secret2": {"isDone": False, "enteredDigit": None},
            "secret3": {"isDone": False, "enteredDigit": None}
        }

        print(f"\nReset: currently on {self.currentPosition}")



    def turnLeft(self, ticks):
        if not isinstance(ticks, int) or ticks <= 0:
            raise ValueError("Ticks must be a positive integer")
        else:
            self.currentPosition = (self.currentPosition - ticks) % 40
            print(f"\nDone turning left: currently on {self.currentPosition}")

            if self.progress["secret1"]["isDone"]:
                self.progress["secret2"]["isDone"] = True
                self.progress["secret2"]["enteredDigit"] = self.currentPosition


    def turnRight(self, ticks):
        if not isinstance(ticks, int) or ticks <= 0:
            raise ValueError("Ticks must be a positive integer")
        
        else:
            self.currentPosition = (self.currentPosition + ticks) % 40
            print(f"\nDone turning right: currently on {self.currentPosition}")

            if not self.progress["secret2"]["isDone"]:
                self.progress["secret1"]["isDone"] = True
                self.progress["secret1"]["enteredDigit"] = self.currentPosition

            else:
                self.progress["secret3"]["isDone"] = True
                self.progress["secret3"]["enteredDigit"] = self.currentPosition
                print("Entered 3 numbers. Try to open it.")



    def open(self):
        enteredDigits = [values["enteredDigit"] for key, values in self.progress.items()]
        # print(enteredDigits, self.combination) # FOR TESTING ONLY
        if enteredDigits != self.combination:
            print("\nLock didn't open. Reset to try again.")
        else:
            print("Successfully opened the lock!")
            sys.exit()


    # def main_menu(self):
        
    #     print("\n1 - Turn Left \n2 - Turn Right \n3 - Open \n4 - Reset \n5 - Exit")
    #     choice = input("\nEnter number of what you want to do:  ")
    #     if choice:
    #         self.controller(choice)
    #     else:
    #         self.main_menu()

    # def controller(self, choice):
    #     if choice not in "12345":
    #         print("\nNumber choice is invalid.\n")
            
    #         while True:
    #             if not (input("Press enter to proceed:  ")):
    #                 return self.main_menu()

    #     if choice == "1":
    #         try:
    #             self.turnLeft(int(input("Turning Left by how many ticks:  ")))

                
    #         except (TypeError, ValueError):
    #             print("\nTicks must be a positive integer.\n")



    #     elif choice == "2":
    #         try:
    #             self.turnRight(int(input("Turning Right by how many ticks:  ")))

    #         except (TypeError, ValueError):
    #             print("\nTicks must be a positive integer.\n")


    #     elif choice == "3":
    #         self.open()


    #     elif choice == "4":
    #         self.reset()

    #     elif choice == "5":
    #         print("CLosing...")
    #         sys.exit()

    #     while True:
    #         if not (input("Press enter to proceed:  ")):
    #             return self.main_menu()

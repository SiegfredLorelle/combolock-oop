class ComboLock:
    def __init__(self, secret1, secret2, secret3):
        self.ComboLock(secret1, secret2, secret3)
        self.reset()
        print(f"\nInstructions: Turn right to first number code, Turn left to second number code, Turn right to third number code.\n")


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

        print(f"Reset: currently on {self.currentPosition}")

    def turnLeft(self, ticks):
        if not isinstance(ticks, int) or ticks <= 0:
            raise ValueError("Ticks must be a positive integer")
        else:
            self.currentPosition = (self.currentPosition - ticks) % 40
            print(f"Done turning left: currently on {self.currentPosition}")

            if self.progress["secret1"]["isDone"]:
                self.progress["secret2"]["isDone"] = True
                self.progress["secret2"]["enteredDigit"] = self.currentPosition

        



    def turnRight(self, ticks):
        if not isinstance(ticks, int) or ticks <= 0:
            raise ValueError("Ticks must be a positive integer")
        
        else:
            self.currentPosition = (self.currentPosition + ticks) % 40
            print(f"Done turning right: currently on {self.currentPosition}")

            if not self.progress["secret2"]["isDone"]:
                self.progress["secret1"]["isDone"] = True
                self.progress["secret1"]["enteredDigit"] = self.currentPosition

            else:
                self.progress["secret3"]["isDone"] = True
                self.progress["secret3"]["enteredDigit"] = self.currentPosition
                print("Entered 3 numbers. Try to open it.")


    def open(self):
        enteredDigits = [values["enteredDigit"] for key, values in self.progress.items()]
        print(enteredDigits, self.combination) # FOR TESTING ONLY
        if enteredDigits != self.combination:
            print("\nLock didn't open. Reset to try again.")

        else:
            print("\nSuccessfully opened the lock!")
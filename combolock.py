class ComboLock:
    def __init__(self, secret1, secret2, secret3):
        self.ComboLock(secret1, secret2, secret3)
        self.reset()
        print(f"\nInstructions: Turn right to first number code, Turn left to second number code, Turn right to third number code.\n")


    def ComboLock(self, secret1, secret2, secret3) : 
        self.combination = (secret1, secret2, secret3)

    
    def __str__(self):
        return f"{self.combination}"





    def reset(self):
        self.currentPosition = 0
        print(f"Reset: currently on {self.currentPosition}")

    def turnLeft(self, ticks):

        self.currentPosition = (self.currentPosition - ticks) % 40
        print(f"Done turning left: currently on {self.currentPosition}")
    
    def turnRight(self, ticks):
        self.currentPosition = (self.currentPosition + ticks) % 40
        print(f"Done turning right: currently on {self.currentPosition}")






    def open(self):
        ...
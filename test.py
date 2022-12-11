# You may uncomment the main menu and controller method in the combolock.py to control via command line

# If main menu and controller is commented, control mannually by calling the methods here

from combolock import ComboLock

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
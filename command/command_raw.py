# Configuration of user input commands
# This file defines the commands that can be executed by the user.
# like: jump, fire gun...
# Simple implementation

BUTTON_X = 0
BUTTON_Y = 1
BUTTON_A = 2
BUTTON_B = 3


def isPressed(button):
    # This function should return True if the button is pressed.
    # For now, we will simulate button presses.
    # In a real implementation, this would check the actual state of the button.
    return False  # Placeholder for actual button state checking logic


def jump():
    print("Jumping!")


def fire_gun():
    print("Firing gun!")


def swapWeapon():
    print("Swapping weapon!")


def lurchIneffectively():
    print("Lurching ineffectively!")


# Called once per frame to handle user input by the game loop
# Hard-code user input commands
def handle_imput():
    if isPressed(BUTTON_X):
        jump()
    elif isPressed(BUTTON_Y):
        fire_gun()
    elif isPressed(BUTTON_A):
        swapWeapon()
    elif isPressed(BUTTON_B):
        lurchIneffectively()


# Implemenation of the Command Pattern
class ICommand:
    def execute(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class JumpCommand(ICommand):
    def execute(self):
        jump()


class FireGunCommand(ICommand):
    def execute(self):
        fire_gun()


class SwapWeaponCommand(ICommand):
    def execute(self):
        swapWeapon()


class LurchIneffectivelyCommand(ICommand):
    def execute(self):
        lurchIneffectively()


class InputHandler:
    def __init__(self, commands=None):
        # Default commands if none are provided
        if not commands:
            commands = {
                # The JumpCommand has to know how to jump the player
                BUTTON_X: JumpCommand(),
                BUTTON_Y: FireGunCommand(),
                BUTTON_A: SwapWeaponCommand(),
                BUTTON_B: LurchIneffectivelyCommand(),
            }
        self._commands = commands

    def handle_input(self):
        for button, command in self._commands.items():
            if isPressed(button):
                command.execute()


# Doing the same, but now passing the GameActor to the commands
class ICommandWithActor:
    def execute(self, actor):
        raise NotImplementedError("This method should be overridden by subclasses")


# THe character that will suffer the actions
class GameActor:
    def jump(self):
        print("GameActor is jumping!")

    def fire_gun(self):
        print("GameActor is firing gun!")

    def swap_weapon(self):
        print("GameActor is swapping weapon!")

    def lurch_ineffectively(self):
        print("GameActor is lurching ineffectively!")


class JumpCommandWithActor(ICommandWithActor):
    def execute(self, actor: GameActor):
        actor.jump()  # Here you would typically use actor to perform the jump


class FireGunCommandWithActor(ICommandWithActor):
    def execute(self, actor: GameActor):
        actor.fire_gun()  # Here you would typically use actor to perform the fire gun action


class SwapWeaponCommandWithActor(ICommandWithActor):
    def execute(self, actor: GameActor):
        actor.swap_weapon()  # Here you would typically use actor to perform the swap weapon action


class LurchIneffectivelyCommandWithActor(ICommandWithActor):
    def execute(self, actor: GameActor):
        actor.lurch_ineffectively()  # Here you would typically use actor to perform the lurch action


class InputHandlerStateless:
    def __init__(self, commands=None):
        # Default commands if none are provided
        if not commands:
            commands = {
                BUTTON_X: JumpCommandWithActor(),
                BUTTON_Y: FireGunCommandWithActor(),
                BUTTON_A: SwapWeaponCommandWithActor(),
                BUTTON_B: LurchIneffectivelyCommandWithActor(),
            }
        self._commands = commands

    # Just returns the commands
    def handle_input(self):
        if isPressed(BUTTON_X):
            return self._commands.get(BUTTON_X)
        elif isPressed(BUTTON_Y):
            return self._commands.get(BUTTON_Y)
        elif isPressed(BUTTON_A):
            return self._commands.get(BUTTON_A)
        elif isPressed(BUTTON_B):
            return self._commands.get(BUTTON_B)
        return None


command = InputHandlerStateless().handle_input()
if command:
    command.execute(GameActor())  # Pass the GameActor to the command

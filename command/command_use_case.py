# Configuration of user input commands
# This file defines the commands that can be executed by the user.
# like: jump, fire gun...
# Simple implementation

BUTTON_X = "x"
BUTTON_Y = "y"
BUTTON_A = "a"
BUTTON_B = "b"


def isPressed(user_input, button):
    return str(user_input) == button


# Doing the same, but now passing the GameActor to the commands
class ICommandWithActor:
    def execute(self, actor):
        raise NotImplementedError("This method should be overridden by subclasses")


# THe character that will suffer the actions
class BaseGameActor:
    def jump(self):
        print("GameActor is jumping!")

    def fire_gun(self):
        print("GameActor is firing gun!")

    def swap_weapon(self):
        print("GameActor is swapping weapon!")

    def lurch_ineffectively(self):
        print("GameActor is lurching ineffectively!")


class JumpCommandWithActor(ICommandWithActor):
    def execute(self, actor: BaseGameActor):
        actor.jump()  # Here you would typically use actor to perform the jump


class FireGunCommandWithActor(ICommandWithActor):
    def execute(self, actor: BaseGameActor):
        actor.fire_gun()  # Here you would typically use actor to perform the fire gun action


class SwapWeaponCommandWithActor(ICommandWithActor):
    def execute(self, actor: BaseGameActor):
        actor.swap_weapon()  # Here you would typically use actor to perform the swap weapon action


class LurchIneffectivelyCommandWithActor(ICommandWithActor):
    def execute(self, actor: BaseGameActor):
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
    def handle_input(self, user_input):
        if isPressed(user_input, BUTTON_X):
            return self._commands.get(BUTTON_X)
        elif isPressed(user_input, BUTTON_Y):
            return self._commands.get(BUTTON_Y)
        elif isPressed(user_input, BUTTON_A):
            return self._commands.get(BUTTON_A)
        elif isPressed(user_input, BUTTON_B):
            return self._commands.get(BUTTON_B)
        return None


class EasyActor(BaseGameActor):
    def jump(self):
        print("EasyActor is jumping easily!")

    def fire_gun(self):
        print("EasyActor is firing gun easily!")

    def swap_weapon(self):
        print("EasyActor is swapping weapon easily!")

    def lurch_ineffectively(self):
        print("EasyActor is lurching ineffectively easily!")


class HardActor(BaseGameActor):
    def jump(self):
        print("HardActor is jumping hard!")

    def fire_gun(self):
        print("HardActor is firing gun hard!")

    def swap_weapon(self):
        print("HardActor is swapping weapon hard!")

    def lurch_ineffectively(self):
        print("HardActor is lurching ineffectively hard!")


easy_actor = EasyActor()
hard_actor = HardActor()
while True:
    user_input = input("Press a button (X, Y, A, B) or 'q' to quit: ").strip().lower()
    if user_input == "q":
        break
    command = InputHandlerStateless().handle_input(user_input)
    if command:
        command.execute(EasyActor())  # Pass the GameActor to the command

JUMP_VELOCITY = 1
IMAGE_JUMP = "jump.png"
IMAGE_DUCK = "dick.png"
IMAGE_STAND = "stand.png"
IMAGE_DIVE = "dive.png"
MAX_CHARGE = 100


class Heroine:
    is_jumping = False
    is_ducking = False
    def handle_input(self, input):
        # Bug: If pressing B she will float forever
        if input == "B":
            if not self.is_jumping and not self.is_ducking:
                self.is_jumping = True
                y_velocity = JUMP_VELOCITY
                self.set_graphics(IMAGE_JUMP)
        elif input == "PRESS_DOWN":
            if not self.is_jumping:
                self.is_ducking = True
                self.set_graphics(IMAGE_DUCK)
        elif input == "RELEASE_DOWN":
            if self.is_ducking:
                self.is_ducking = False
                self.set_graphics(IMAGE_STAND)

    def set_graphics(image):
        pass

# Using Enums
# It gives some improvements in the code, but it is still hard to change things
from enum import Enum
class State(Enum):
    STATE_STANDING = True
    STATE_JUMPING = False
    STATE_DUCKING = False
    STATE_DIVING = False

class Heroine:
    def __init__(self):
        self._state = State.STATE_STANDING
        self._charge_time = 0
    # Now swicht by state, not by inputs (buttons)
    def handle_input(self, input):
        match input:
            case State.STATE_STANDING:
                if (input == "PRESS_B"):
                    self._state = State.STATE_JUMPING
                    self.charge_time = 0
                    yVelocity_ = JUMP_VELOCITY
                    self.set_graphics(IMAGE_JUMP)
                elif (input == "PRESS_DOWN"):
                    state_ = State.STATE_DUCKING
                    self.set_graphics(IMAGE_DUCK)
            case State.STATE_JUMPING:
                if (input == "PRESS_DOWN"):
                    state_ = State.STATE_DIVING
                    self.set_graphics(IMAGE_DIVE)
            case State.STATE_DUCKING:
                if input == "RELEASE_DOWN":
                    state_ = State.STATE_STANDING
                    self.set_graphics(IMAGE_STAND)
    def set_graphics(self):
        pass

    def update(self):
        # charge while the heroine is duking
        if self._state == State.STATE_DUCKING:
            self.charge_time += 1
            if self.charge_time > MAX_CHARGE:
                self.super_bomb()

    def super_bomb(self):
        pass

# Using State Pattern
class Heroine:
    def __init__(self):
        self.state = None
    def handle_input(self, input):
        # Calls the HeroineState handle_input method
        state = self.state.hander_input(self, input)
        if self.state != None:
            self.state = state
            # Call the enter action on the new state.
            self.state.enter(self)
    def set_graphics(self):
        pass

    def update(self):
        self.state.update(self)

    def super_bomb(self):
        pass


class HeroineState:
    def __init__(self):
        self.charge_time = 0
    def handle_input(self, heroine: Heroine, input) -> "HeroineState":
        pass
    def update(self, heroine: Heroine):
        pass
    def enter(self):
        pass

class StandingState(HeroineState):
    def enter(self, heroine: Heroine):
        heroine.set_graphics(IMAGE_STAND)

class DuckingState(HeroineState):
    def handle_input(self, heroine: Heroine, input):
        if (input == "RELEASE_DOWN"):
            return StandingState()

    def update(self, heroine: Heroine):
        if self.charge_time > MAX_CHARGE:
            heroine.super_bomb()

# Concurrent state machines
# We need to define states for the Heroine when she is armed and unarmed. So, we need two
# state machines: one for movements and other for what shes is carring
class Heroine:
    def __init__(self):
        self._state = None
        self._equipment = None # other state machine

    def handle_input(self, input):
        # When the heroine delegates inputs to the states, she hands it to both of them
        self._state.handle_input(self, input)
        self._equipment.handle_input(self, input)

# Hierarchical State Machines
# Define a base state class
class OnGroundState(HeroineState):
    def handle_input(self, heroine, input):
        if input == "PRESS_B":
            print("jump")
        elif input == "PRESS_DOWN":
            print("duck")



class DuckingState(OnGroundState):
    def handle_input(self, heroine, input):
        if input == "RELEASE_DOWN":
            print("stand up")
        else:
            # Didn't handle input, so walk up hierarchy.
            OnGroundState().handle_input(heroine, input)

# Pushdown automata
# if we need the Heroine is stading ahd has to transt to a given state, lets say, firing, and need to
# go back to the previous state, we can use a stack to push and pod the current states.
# Possible implementation
class Heroine:
    def __init__(self):
        self._state = None
        # Stores the current state in a stack
        self._stack = [self._state]
    def handle_state(self, input):
        next_state = self._state.get_next_state()
        # Stores the new state on top of the stack
        self._stack.append(next_state)
        # Do the stuff
        next_state.handle_input(input)
        # Remove the top most state and go back to the previous one
        self._stack.pop(next_state)

# Other references
# https://medium.com/@vedantchaudhari/goal-oriented-action-planning-34035ed40d0b
# http://web.archive.org/web/20140402204854/http://www.altdevblogaday.com/2011/02/24/introduction-to-behavior-trees/
# Achievement unlocked
GRAVITY = (0, -9.81)
EVENT_START_FALL = "start_fall"


def update_entity(self, entity):
    was_on_surface = entity.is_on_surface()
    entity.accelerate(GRAVITY)
    entity.update()

    if was_on_surface and not entity.is_on_surface():
        self.notify(entity, EVENT_START_FALL)


# Observer pattern implementation
class Observer:
    def on_notify(self, entity, event):
        raise NotImplementedError("This method should be overridden by subclasses")


class AchievementSystem(Observer):
    heroIsOnBridge = True

    def on_notify(self, entity, event):
        if event == EVENT_START_FALL:
            if entity.isHero() and self.heroIsOnBridge:
                self.unlockAchievement("Leap of Faith")
        # handle other events here

    def unlockAchievement(self, achievement_name):
        # if not already unlocked
        print(f"Achievement Unlocked: {achievement_name}")


# the subject being observed
class Subject:
    observers = []
    nun_observers: int = 0

    def add_observer(self, observer: Observer):
        self.observers.append(observer)
        self.nun_observers += 1

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
        self.nun_observers -= 1

    def notify(self, entity, event):
        for observer in self.observers:
            observer.on_notify(entity, event)


class Physics(Subject):
    def __init__(self):
        super().__init__()
        self.velocity = (0, 0)
        self.position = (0, 0)
        self.on_surface = True  # Simplified for this example

    def accelerate(self, acceleration):
        self.velocity = (self.velocity[0] + acceleration[0], self.velocity[1] + acceleration[1])

    def update_entity(self, entity):
        pass


# The observers subcribe to the subject using the public add_observer method
#  and get notified when something happens


# Linked Observers pattern implementation
# On observer can notify other observers


class LinkedObserver:
    next: Observer = None


class SubjectLinked:
    head: LinkedObserver = None

    def add_observer(self, observer: LinkedObserver):
        observer.next = self.head
        self.head = observer

    def remove_observer(self, observer: LinkedObserver):
        if self.head == observer:
            # Updates the head with the next observer
            self.head = self.head.next
            # Remove the observer from the chain of observers
            observer.next = None
            return
        current = self.head
        while current and current.next != observer:
            current = current.next
        if current and current.next == observer:
            current.next = current.next.next

    def notify(self, entity, event):
        current = self.head
        while current:
            current.on_notify(entity, event)
            # Replaces the current observer with the next one and notifies it in the next loop
            current = current.next

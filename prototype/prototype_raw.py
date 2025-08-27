class Monster:
    pass

class Ghost(Monster):
    pass

class Demon(Monster):
    pass

class Sorcerer(Monster):
    pass

# Spawners
class Spawner:
    def monster_spawner(self) -> Monster:
        pass

class GhostSpawner(Spawner):
    def monster_spawner(self):
        return Ghost()
    
class DemonSpawner(Spawner):
    def monster_spawner(self):
        return Demon()


class SorcererSpawner(Spawner):
    def monster_spawner(self):
        return Sorcerer()
    

# Using prototype
class Monster:
    def clone(self):
        pass

class Ghost(Monster):
    def __init__(self, health, speed):
        self._health = health
        self._speed = speed

    def clone(self):
        return Ghost(self._health, self._speed)


# Just one spawner for all kind of monsters
class Spawner:
    def __init__(self, prototype: Monster):
        self._prototype = prototype

    def spawn_monster(self) -> Monster:
        return self._prototype.clone()
    

ghost_prototype: Monster = Ghost(15, 3)
ghost_spawner = Spawner(ghost_prototype)
new_monster = ghost_spawner.spawn_monster()